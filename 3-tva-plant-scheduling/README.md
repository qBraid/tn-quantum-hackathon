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
4. Early on, one teammate works through [`qaoa_primer.ipynb`](./qaoa_primer.ipynb) (the 6-node part, about 45 minutes) while the rest start milestones 1 and 2. It shows QAOA's three pieces (cost layer, mixer, optimizer) on a textbook problem, Max-Cut.

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
| `check_schedule(plants, demand, reserve, schedule, milp_cost=None)` | Scores a day: total cost and a table of broken rules. Pass `milp_cost` to also see the gap to the optimum |
| `check_hour(plants, demand_mw, reserve_mw, choice, was_on=...)` | Scores one hour's on/off choice and says whether it's the best of all 32 ("Match!"), without showing the best one |
| `locks(plants, history)` | Which plants min up/down times force on or off next hour |

Run `%run check.py` in a notebook cell for a short demo.

## Milestones

| # | Milestone | Time | What you do | Done when |
|---|---|---|---|---|
| 1 | Understand it | ~1 h | Plot demand. Hand-schedule the 5 plants for 6 hours (in the notebook or a spreadsheet). | You have a schedule and its cost. |
| 2 | Classical baseline | 2 to 3 h | Run the mixed-integer program for 5 plants over 24 hours (provided; read it). Write the cheapest-plants-first rule (TODO 1). | You have the optimal daily cost and the rule's gap from it. |
| 3 | Code the quantum cost function | 1 to 2 h | One hour's problem is 5 on/off qubits plus 3 helper (slack) qubits for the safety-margin rule. Write the plant costs (TODO 2) and the QUBO (TODO 3). Check it with the checker. | Its cheapest answer matches the best choice for that hour (the checker prints "Match!"), and you can say in one sentence how the primer's Max-Cut cost relates to yours. |
| 4 | Run it hour by hour | 4 to 5 h | QAOA for each hour on the simulator, carrying results forward. Startup costs and min on/off times are checked classically. Then tune: layers, shots, penalty weight, warm starts. | You have the daily cost vs the baseline and a table of any rules broken. |
| 5 | IonQ hardware run | ~2 h, early (queues can take hours) | One hour's 8-qubit problem at 100 to 200 shots, after tuning on IonQ's free simulator with its noise model on. | You have the job ID and a chart comparing hardware vs simulator. |
| 6 | Tell the story | ~2 h | The cost gap, how often answers were valid, time including the hardware queue, and what would have to change for quantum to help. | You can walk a judge through your results in 5 minutes. |

Words you will meet:
- **QUBO**: a cost function over 0/1 variables with only single and pair terms. QAOA needs the problem in this form.
- **Slack (helper) qubits**: extra bits that turn a "≥" rule into an exact equation the QUBO can penalize.
- **MILP**: mixed-integer linear program, the standard classical tool for this problem.

## What judges look for

On Sunday morning, you present your pitch deck to this track's judges, and they ask you to walk them through your work. Understanding and clarity count most: why your QUBO works, what the hour-by-hour loop does, and what your results mean for a utility. Code counts less. See the [main README](../README.md#what-judges-look-for).

**Due Sunday 9:00 AM:** your pitch deck and your code as a ZIP ([what to submit, and where](../README.md#what-to-submit)). Have your notebook and any tools you built, run with their outputs and your IonQ job IDs. Be ready to explain:
- **Your solution:** your daily cost against the exact baseline and the cheapest-first rule, how often your answers were valid, any rules broken, and the hardware result next to the simulator.
- **Customer and value proposition:** what a utility like TVA would gain (or not) from your approach, including time spent waiting in the hardware queue.
- **What you learned:** where quantum honestly stands on this problem (see below).
- **What didn't work:** if something failed or you couldn't find a solution, say so clearly and explain why. That earns points.

**The notebook is a starter.** Add your own code, cells and notebooks, try a different approach, and expand as far as you like.

**Tools worth building** (they count):
- a schedule viewer: the 24-hour plan as a chart, with every broken rule flagged;
- a "what if" tool: change demand, fuel prices or the reserve and re-solve;
- a dashboard that compares the exact solver, your rule and QAOA, including cost and time;
- a visual of how QAOA's answer for one hour changes with layers, shots or noise.

## Hardware rules

- Hardware: IonQ Forte through qBraid, device `ionq:ionq:qpu:forte-1`.
- Tune on the simulator first. Practice on IonQ's free simulator, `ionq:ionq:sim:simulator`, with `runtime_options={"noise_model": "forte-1"}` (the notebook's hardware cell is set up for this).
- Run only your final, tuned circuit on hardware. At most 200 shots per hardware run.
- Send hardware runs early. Queues can take hours, so aim for Saturday, not Sunday morning.
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

Say plainly where quantum stands, with your own numbers. It won't cost you points; it earns them. Answer these in your story:

- How long does the exact solver take on 5 plants, and on the 10-plant version? How long does your hour-by-hour QAOA take, including the hardware queue?
- One hour has 32 on/off choices. How does QAOA compare with simply checking all of them, or with a couple hundred random guesses? The notebook runs a random-guess comparison: what does it tell you, and which step of the loop is really doing the work?
- What does solving hour by hour miss, compared with planning the whole day at once?
- What would have to change for quantum to help on unit commitment?

Reading: Koretsky et al. (2021, [arXiv:2110.12624](https://arxiv.org/abs/2110.12624)) ran QAOA on single-hour unit commitment with 6 to 10 plants. What did they conclude about when classical solvers stop being enough?

A team that shows where its hybrid approach lost cost or broke a rule, and explains why, should score well.

## Files

| File | What it is |
|---|---|
| `README.md` | This page |
| `starter.ipynb` | The starter notebook: scaffold, TODOs, QAOA loop, hardware cell |
| `qaoa_primer.ipynb` | QAOA on Max-Cut, the textbook example (milestone 3; the 12-node part is optional) |
| `check.py` | Data loader, schedule checker, MILP baseline |
| `data/` | Plants, demand, source and license notes |

## Links

- RTS-GMLC test system: https://github.com/GridMod/RTS-GMLC (TVA's recommended data; see also the [Reliability Test System page](https://www.nlr.gov/grid/reliability-test-system), and Prescient's [guide to the generator file's columns](https://prescient.readthedocs.io/en/stable/reference/file_formats/rts-gmlc/gen.html))
- Smaller MATPOWER instances TVA suggested, such as `case24_ieee_rts`: https://matpower.app/manual/matpower/ExamplematpowerCases.html (MATPOWER's function and case reference: https://matpower.org/docs/ref/matpower5.0/menu5.0.html)
- Koretsky et al., "Adapting Quantum Approximation Optimization Algorithm (QAOA) for Unit Commitment", 2021: https://arxiv.org/abs/2110.12624
- QAOA primer (part of milestone 3): [`qaoa_primer.ipynb`](./qaoa_primer.ipynb)
- The qBraid Award is open to every team (optional): `../4-qbraid-award/`
