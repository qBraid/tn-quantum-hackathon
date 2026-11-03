# Grid Sensor Placement (TVA)

**Sponsor:** TVA (Tennessee Valley Authority) · **Platform:** qBraid · **Hardware:** IonQ Forte

## The problem

TVA's grid is a network of substations joined by power lines. A PMU (phasor measurement unit) is a sensor that takes time-synchronized measurements, so operators can tell what state the grid is in. A PMU at a substation sees that substation and every substation directly connected to it.

PMUs are expensive. **What is the smallest set of substations that lets operators see every substation?**

**Everyday version:** put security cameras at intersections so that every intersection is visible from at least one camera. Computer scientists call this the *minimum dominating set* problem. It maps naturally onto qubits: one qubit per substation, where 1 means "put a sensor here".

## Background from TVA

TVA shared NERC's *Reliability Guideline: PMU Placement and Installation* (December 2016) as background for this track. Three ideas from it shape the problem:

1. **There are two ways to state the goal.** You can find the fewest PMUs that make the whole grid observable, which is milestones 2 to 5. Or you can find the most observability you can get from a fixed number of PMUs, which is the "fixed budget" stretch goal.
2. **Losing one PMU, or its data feed, can leave part of the grid unseen.** That's why utilities plan for redundancy, which is the N-1 stretch goal.
3. **Utilities don't treat every substation the same.** They score each candidate location by how many monitoring applications a PMU there would serve, such as state estimation, oscillation monitoring and angle monitoring, with a weight for each application. That's the priority-weights stretch goal.

## Start here

1. Open `starter.ipynb` in qBraid Lab with the qBraid SDK environment's kernel.
2. Run the cells from the top.
3. Do the TODOs (there are 3). Each one has a hint.

Optional QAOA primer: `../0-warm-up/qaoa_islanding.ipynb`.

## The data

| File | What it is |
|---|---|
| `data/ieee14.json` | IEEE 14-bus test grid: 14 substations, 20 lines. The main grid. |
| `data/ieee14_piece6.json` | A 6-substation piece of it, small enough for quantum hardware |
| `data/ieee30.json` | IEEE 30-bus test grid, for the stretch goal |

A *bus* is a substation. Each file lists the buses, the lines, the zero-injection buses (see stretch goals), the power plant buses and each bus's load. See `data/README.md` for sources.

`check.py` checks any placement: is it valid, which substations are unseen, how sturdy it is, and (for grids of 20 buses or fewer) how far it is from the fewest possible. Run `python check.py` for a demo.

## Milestones

| # | Milestone | Time | What you do | Done when |
|---|---|---|---|---|
| 1 | Understand it | about 1 h | Draw the grid and place sensors by hand | you have a placement and one sentence on what a PMU sees |
| 2 | Classical baseline | 2 to 3 h | A greedy rule and an exact integer program | you have the optimal count and its runtime |
| 3 | Code the quantum cost function | 1 to 2 h | The number of sensors plus a large penalty for every unseen substation. Check it with the checker on the 6-substation piece. | its cheapest answer matches the integer program |
| 4 | Run QAOA | 3 to 4 h | On the simulator: first the 6-substation piece, then all 14 | you have a chart of how often QAOA finds an optimal placement and how often it leaves a substation unseen |
| 5 | IonQ hardware run | about 2 h, by **Sat 9 PM** | The 6-substation piece at 100 to 200 shots, after tuning on IonQ's free noise simulator | you have the job ID and a chart comparing hardware with the simulator |
| 6 | Tell the story | about 2 h | What the sensors cost, what an operator gains, and where quantum honestly stands | you can walk a judge through your results in 5 minutes |

Why a 6-substation piece for hardware: the full 14-substation QAOA circuit needs over 300 two-qubit gates, far more than today's hardware runs well. The piece needs a few dozen.

## What to submit (by Sunday 9:00 AM)

**Your notebook:** `starter.ipynb` with the TODOs done, run top to bottom, with your IonQ job IDs.

### For the judges' visit and the finalist deck

Judges visit your team on Sunday morning, and selected teams present a 5-slide deck at the closing ceremony (see the [main README](../README.md#judging-and-the-finalist-deck)). Have these ready either way:

- **Solution:** your sensor locations, the count and the coverage (from `check_placement`); what happens if one sensor fails (`breaks_if_lost`, or the N-1 check); greedy vs integer program vs QAOA (count, runtime, how often QAOA finds the best answer); and the hardware result next to the simulator.
- **Customer and Value Proposition:** what a sensor costs and what a grid operator gains. A 2014 U.S. Department of Energy report, [Factors Affecting PMU Installation Costs](https://www.energy.gov/oe/articles/factors-affecting-pmu-installation-costs-october-2014), is a good starting point for costs.
- **What We Learned:** where quantum honestly stands on this problem (see below).

## Hardware rules

- **Tune on simulators first:** the local Aer simulator, then IonQ's free noise simulator (`ionq:ionq:sim:simulator` with `noise_model="aria-1"`). The notebook's hardware cell is set up for this.
- **Real hardware is IonQ Forte** (`ionq:ionq:qpu:forte-1`) through qBraid. Run only your final, tuned circuit.
- **Cap every hardware run at 200 shots.**
- **Hardware runs close Saturday 9 PM.**
- **If IonQ is down or the queue isn't moving,** keep your job ID and your noisy-simulator result to show judges, and ask a qBraid mentor about IQM Garnet (`aws:iqm:qpu:garnet`) as a backup.
- Keep the hardware circuit to a few dozen two-qubit gates. The notebook prints the count.

## Stretch goals (pick any)

- **Zero-injection buses.** A zero-injection bus has no load and no generator, so the power flowing in equals the power flowing out. That lets operators work out one unseen neighbor without a sensor. IEEE 14 bus 7 is one. Use `check_placement(grid, chosen, zib=True)`. How many sensors does the rule save?
- **N-1 (every substation seen twice).** The grid stays fully visible if any one sensor fails. Use `check_placement(grid, chosen, n1=True)` and `ilp_placement(grid, twice=True)`. For QAOA, add a penalty for each substation seen only once.
- **Fixed budget.** With only *k* sensors (try k = 2 or 3 on IEEE 14), place them to see as many substations as possible. This is the second goal in NERC's guideline. How does the cost function change when you can't afford full coverage?
- **Priority weights.** Some substations matter more, such as big loads, power plants and the links between regions. Build a small priority table the way NERC's guideline suggests (a weight per application, times whether a PMU at that bus serves it), then give high-priority buses a bigger penalty or require them to be seen twice. See how the placement changes.
- **30 substations on qBraid's GPU simulator.** Load `data/ieee30.json`. The exact table of 2^30 costs no longer fits in memory, so switch to sampled shots.

## Honest quantum value

Classical solvers handle grids this size instantly: the integer program in the notebook finds the best placement for 14 substations in milliseconds. In a 2020 study (Jones et al., [arXiv 2001.04489](https://arxiv.org/abs/2001.04489)), a D-Wave quantum annealer matched the best placement on grids up to 30 substations and fell short at 39 and 57.

So quantum computers do not beat classical methods on this problem today. The learning is in building and testing the whole pipeline: turning a grid rule into a cost function, then a circuit, then running it on a simulator and on real hardware, and comparing it honestly with classical methods. Say this plainly in your deck.

## Links

- MATPOWER IEEE 14-bus case: <https://github.com/MATPOWER/matpower/blob/master/data/case14.m>
- MATPOWER IEEE 30-bus case: <https://github.com/MATPOWER/matpower/blob/master/data/case_ieee30.m>
- UW Power Systems Test Case Archive (the original IEEE cases): <https://labs.ece.uw.edu/pstca/>
- Background reading from TVA: NERC's *Reliability Guideline: PMU Placement and Installation* (December 2016)
- Data sources TVA pointed to:
  - an [IEEE overview of PMU placement](https://ieeexplore.ieee.org/document/7459248)
  - [IEEE 14-bus PMU measurements at optimal and sub-optimal locations](https://ieee-dataport.org/documents/pmu-measurements-optimal-sub-optimal-locations-ieee-14-bus-system) (IEEE DataPort)
  - the larger MATPOWER cases (57, 118 and 300 buses) in the [MATPOWER data folder](https://github.com/MATPOWER/matpower/tree/master/data)
- Jones et al. 2020, quantum annealing for PMU placement: <https://arxiv.org/abs/2001.04489>

## The qBraid Award

The qBraid Award is open to every team. It's optional; see `../4-qbraid-award/`.
