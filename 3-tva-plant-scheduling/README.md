# Power Plant Scheduling (TVA)

## The problem

Every day TVA decides which power plants to switch on for each hour of tomorrow, so supply covers demand plus a safety margin. Big plants are cheap per megawatt but expensive to start and slow to change. Small plants start fast but cost more to run. The on/off choices are a hard yes-or-no puzzle. Once they are made, setting each plant's output is easy classical math.

Power engineers split the job in two:
- **Unit commitment** decides which plants are online each hour (the yes-or-no part, where your quantum work goes).
- **Economic dispatch** decides how much each online plant produces (classical; `check.py` does it for you).

What drives the choices:
- A plant's **marginal cost** (cost of one more MWh) is roughly heat rate × fuel price + variable operating cost.
- Big thermal plants (coal, combined-cycle gas) have low marginal cost but high **startup cost**, and **minimum up and down times**: once on they must stay on for hours, and once off they must stay off.
- **Peakers** (small gas or oil turbines) start fast but cost more per MWh.
- Every plant that is on also pays a **no-load cost** per hour, just for running.

## Background from TVA

TVA shared an overview of how utilities make these decisions. The short version:

1. **Forecast** load, wind and solar.
2. **Set the requirements:** the energy needed each hour, plus reserves for surprises.
3. **Commit:** choose which units are on.
4. **Dispatch** the committed units, cheapest first.
5. **Check the grid can carry it.**
6. **Re-optimize** as conditions change.

The cost TVA cares about is the whole day's: fuel, startups, no-load and operating costs. It isn't just the cost of the next megawatt.

In TVA's example of loading the cheapest units first, the order is wind ($0/MWh), nuclear ($10), coal ($25), then gas combined cycle ($40). Gas is the *marginal* unit, the one that sets the price, because it supplies the last megawatts needed.

TVA also pointed teams to RTS-GMLC as the best open data for this. Use its source CSV files and hourly time series for day-long schedules. Its MATPOWER file is a single peak-hour snapshot with renewables switched off. Our `data/` files come from those CSVs.

## Everyday version

A pizzeria with several ovens. Big ovens are cheap per pizza but take hours to preheat and must stay on once lit. Small ovens heat instantly but cost more per pizza. You plan tomorrow's ovens against an hourly order forecast plus a buffer.

## Start here

1. Open `starter.ipynb` in qBraid Lab with the qBraid SDK environment's kernel.
2. Run the cells from the top. They load the data, plot it and solve the classical baseline.
3. Fill in the TODOs: **TODO 1** cheapest-first rule, **TODO 2** cost of one plant for one hour, **TODO 3** the QUBO. Every cell after them already works and uses your code.
4. New to QAOA? The optional primer is `../0-warm-up/qaoa_islanding.ipynb`.

## The data

| File | What it is |
|---|---|
| `data/plants.csv` | 5 plants: COAL (350 MW), GAS_CC (350 MW), PEAKER_A, PEAKER_B and OIL (50 MW each) |
| `data/demand.csv` | 24 hourly demand values (MW) and the reserve (10% of demand) |
| `data/plants10.csv`, `data/demand10.csv` | The 10-plant stretch version |

Every plant is built from a real unit in the RTS-GMLC test grid, with its real startup cost, min on/off times, ramp rate and fuel costs. `data/README.md` explains the source, license and every step of how the numbers were made.

The rules, each hour:
- Every plant that is on makes between its `pmin_mw` and `pmax_mw`, and total output equals demand.
- The capacity of the plants that are on (sum of `pmax_mw`) is at least demand + reserve.
- A plant that switches on stays on at least `min_up_h` hours. One that switches off stays off at least `min_down_h` hours.
- At midnight only COAL is running.
- Daily cost = startup costs + no-load costs + energy costs.

## The checker (`check.py`)

| Function | What it does |
|---|---|
| `load_plants()`, `load_demand()` | Read the CSV files |
| `solve_milp(plants, demand, reserve)` | The classical baseline: an exact mixed-integer program (scipy `milp`). Returns cost, schedule, dispatch, seconds |
| `check_schedule(plants, demand, reserve, schedule)` | Scores a day: total cost, gap vs the MILP optimum, and a table of broken rules |
| `check_hour(plants, demand_mw, reserve_mw, choice, was_on=...)` | Scores one hour's on/off choice against the brute-force best of all 32 choices |
| `locks(plants, history)` | Which plants min up/down times force on or off next hour |

Run `python check.py` for a short demo.

## Milestones

| # | Milestone | Time | What you do | Done when |
|---|---|---|---|---|
| 1 | Understand it | ~1 h | Plot demand. Hand-schedule the 5 plants for 6 hours (in the notebook or a spreadsheet). | You have a schedule and its cost. |
| 2 | Classical baseline | 2 to 3 h | Run the mixed-integer program for 5 plants over 24 hours (provided; read it). Write the cheapest-plants-first rule (TODO 1). | You have the optimal daily cost and the rule's gap from it. |
| 3 | Code the quantum cost function | 1 to 2 h | One hour's problem is 5 on/off qubits plus 3 helper (slack) qubits for the safety-margin rule. Write the plant costs (TODO 2) and the QUBO (TODO 3). Check it with the checker. | Its cheapest answer matches the best choice for that hour (the checker prints "Match!"). |
| 4 | Run it hour by hour | 4 to 5 h | QAOA for each hour on the simulator, carrying results forward. Startup costs and min on/off times are checked classically. Then tune: layers, shots, penalty weight, warm starts. | You have the daily cost vs the baseline and a table of any rules broken. |
| 5 | IonQ hardware run | ~2 h, by Sat 9 PM | One hour's 8-qubit problem at 100 to 200 shots, after tuning on IonQ's free noise simulator. | You have the job ID and a chart comparing hardware vs simulator. |
| 6 | Tell the story | ~2 h | The cost gap, how often answers were valid, time including the hardware queue, and what would have to change for quantum to help. | You can walk a judge through your results in 5 minutes. |

Words you will meet:
- **QUBO**: a cost function over 0/1 variables with only single and pair terms. QAOA needs the problem in this form.
- **Slack (helper) qubits**: extra bits that turn a "≥" rule into an exact equation the QUBO can penalize.
- **MILP**: mixed-integer linear program, the standard classical tool for this problem.

## What to submit (by Sunday 9:00 AM)

**Your notebook:** `starter.ipynb` with your code and outputs, and your IonQ job IDs.

### For the judges' visit and the finalist deck

Judges visit your team on Sunday morning, and selected teams present a 5-slide deck at the closing ceremony (see the [main README](../README.md#judging-and-the-finalist-deck)). Have these ready either way:

- **Solution:** your daily cost against the MILP baseline and the cheapest-first rule, how often your answers were valid, any rules broken, and the hardware result next to the simulator.
- **Customer and Value Proposition:** what a utility like TVA would gain (or not) from your approach, including time spent waiting in the hardware queue.
- **What We Learned:** where quantum honestly stands on this problem (see below).

## Hardware rules

- Hardware: IonQ Forte through qBraid, device `ionq:ionq:qpu:forte-1`.
- Tune on the simulator first. Practice on IonQ's free simulator, `ionq:ionq:sim:simulator` with `noise_model` `aria-1` (the notebook's hardware cell is set up for this).
- Run only your final, tuned circuit on hardware. At most 200 shots per hardware run.
- Hardware runs close **Saturday 9 PM**.
- If IonQ is down or the queue isn't moving, keep your job ID and your noisy-simulator result to show judges, and ask a qBraid mentor about IQM Garnet (`aws:iqm:qpu:garnet`) as a backup.
- The notebook prints your circuit's two-qubit gate count. IonQ advises keeping hardware circuits to a few dozen two-qubit gates, so use one QAOA layer (`p=1`) on hardware.

## Stretch goals (pick any)

- **10 plants.** Use `data/plants10.csv` and `data/demand10.csv`. How many slack qubits does the safety-margin rule need now?
- **Two hours at once.** Put two consecutive hours in one QUBO (16 qubits, more with 10 plants) so QAOA can see startup costs across hours. Bigger versions need qBraid's GPU simulator.
- **Ramp limits.** `solve_milp(..., ramps=True)` and `check_schedule(..., ramps=True)` add them. The RTS-GMLC ramp rates are generous for 1-hour steps, so try tightening them and see what changes.
- **A battery.** Add a storage unit (charge, discharge, state of charge) to the MILP, then decide how it would enter your hour-by-hour loop.
- **Wind and solar.** Subtract RTS-GMLC's hourly wind and solar output from demand to get *net load*, then schedule against that. TVA's overview flags the evening ramp, when solar fades, as a growing challenge.
- **Drop the helper qubits.** Replace the slack penalty with a penalty-only formulation (search "unbalanced penalization QAOA"). Compare qubits, two-qubit gates and how often answers are valid.
- **A better hour cost.** TODO 2's cost is an approximation. Improve it and measure how often the QUBO's best matches the exact best.

## Honest quantum value

Say this plainly in your story. It will not cost you points; it earns them.

- Koretsky et al. (2021, [arXiv:2110.12624](https://arxiv.org/abs/2110.12624)) ran QAOA on single-hour unit commitment problems with 6 to 10 plants. They concluded classical solvers handle this well below about 400 plants.
- A 10-plant, 24-hour version solves in under a tenth of a second classically. Try `solve_milp` on `plants10.csv` and time it.
- One hour here has only 32 on/off choices. A laptop checks all of them instantly, and a couple hundred random guesses usually find the best one. The notebook runs that random-guess comparison next to QAOA so you can see it.
- Solving hour by hour misses savings that come from planning the whole day (like starting a plant early to avoid a second startup), however good the per-hour solver is.

A team that says so, and shows where its hybrid approach lost cost or broke a rule, should score well. So should a team that explains what would have to change for quantum to help.

## Files

| File | What it is |
|---|---|
| `README.md` | This page |
| `starter.ipynb` | The starter notebook: scaffold, TODOs, QAOA loop, hardware cell |
| `check.py` | Data loader, schedule checker, MILP baseline |
| `data/` | Plants, demand, source and license notes |

## Links

- RTS-GMLC test system: https://github.com/GridMod/RTS-GMLC (TVA's recommended data; see also the [Reliability Test System page](https://www.nlr.gov/grid/reliability-test-system))
- Smaller MATPOWER instances TVA suggested, such as `case24_ieee_rts`: https://matpower.app/manual/matpower/ExamplematpowerCases.html
- Koretsky et al., "Adapting Quantum Approximation Optimization Algorithm (QAOA) for Unit Commitment", 2021: https://arxiv.org/abs/2110.12624
- QAOA primer (optional): `../0-warm-up/qaoa_islanding.ipynb`
- The qBraid Award is open to every team (optional): `../4-qbraid-award/`
