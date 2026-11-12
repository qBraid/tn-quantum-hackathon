# Grid Sensor Placement (TVA)

**Sponsor:** TVA (Tennessee Valley Authority) · **Platform:** qBraid · **Hardware:** IonQ Forte

## The problem

TVA's grid is a network of substations joined by power lines. A PMU (phasor measurement unit) is a sensor that takes time-synchronized measurements, so operators can tell what state the grid is in. A PMU at a substation sees that substation and every substation directly connected to it.

PMUs are expensive. **What is the smallest set of substations that lets operators see every substation?**

**Everyday version:** put security cameras at intersections so that every intersection is visible from at least one camera. Computer scientists call this the *minimum dominating set* problem. It maps naturally onto qubits: one qubit per substation, where 1 means "put a sensor here".

## Background from TVA

TVA shared NERC's *Reliability Guideline: PMU Placement and Installation* (December 2016) as background for this track. It's in [`background/`](./background/), with TVA's original problem in TVA's words. Three ideas from it shape the problem:

1. **There are two ways to state the goal.** You can find the fewest PMUs that make the whole grid observable, which is milestones 2 to 5. Or you can find the most observability you can get from a fixed number of PMUs, which is the "fixed budget" stretch goal.
2. **Losing one PMU, or its data feed, can leave part of the grid unseen.** That's why utilities plan for redundancy, which is the N-1 stretch goal.
3. **Utilities don't treat every substation the same.** They score each candidate location by how many monitoring applications a PMU there would serve, such as state estimation, oscillation monitoring and angle monitoring, with a weight for each application. That's the priority-weights stretch goal.

## Start here

1. Open `starter.ipynb` in qBraid Lab with the **qBraid-SDK (v0.12.2)** kernel (pick it in the Select Kernel box).
2. Run the cells from the top.
3. Do the TODOs (there are 3). Each one has a hint.
4. Early on, one teammate works through [`qaoa_primer.ipynb`](./qaoa_primer.ipynb) (the 6-node part, about 45 minutes) while the rest start milestones 1 and 2. It shows QAOA's three pieces (cost layer, mixer, optimizer) on a textbook problem, Max-Cut.

## The data

| File | What it is |
|---|---|
| `data/ieee14.json` | IEEE 14-bus test grid: 14 substations, 20 lines. The main grid. |
| `data/ieee14_piece6.json` | A 6-substation piece of it, small enough for quantum hardware |
| `data/ieee30.json` | IEEE 30-bus test grid, for the stretch goal |

A *bus* is an electrical node in a substation; in these files there's one per substation. Each file lists the buses, the lines, the zero-injection buses (see stretch goals), the power plant buses and each bus's load. See `data/README.md` for sources.

`check.py` checks any placement: is it valid, which substations are unseen, and how sturdy it is. Once you have your own answer, `check_placement(grid, chosen, compare=True)` also says how far it is from the fewest possible (grids of 20 buses or fewer). Run `%run check.py` in a notebook cell for a demo.

## Milestones

| # | Milestone | Time | What you do | Done when |
|---|---|---|---|---|
| 1 | Understand it | about 1 h | Draw the grid and place sensors by hand | you have a placement and one sentence on what a PMU sees |
| 2 | Classical baseline | 2 to 3 h | A greedy rule and an exact integer program | you have the optimal count and its runtime |
| 3 | Code the quantum cost function | 1 to 2 h | The number of sensors plus a large penalty for every unseen substation. Check it with the checker on the 6-substation piece. | its cheapest answer matches the integer program, and you can say in one sentence how the primer's Max-Cut cost relates to yours |
| 4 | Run QAOA | 3 to 4 h | On the simulator: first the 6-substation piece, then all 14 | you have a chart of how often QAOA finds an optimal placement and how often it leaves a substation unseen |
| 5 | IonQ hardware run | about 2 h, early (queues can take hours) | The 6-substation piece at 100 to 200 shots, after tuning on IonQ's free simulator with its noise model on | you have the job ID and a chart comparing hardware with the simulator |
| 6 | Tell the story | about 2 h | What the sensors cost, what an operator gains, and where quantum honestly stands | you can walk a judge through your results in 5 minutes |

Why a 6-substation piece for hardware: the full 14-substation QAOA circuit needs over 300 two-qubit gates per layer, far more than today's hardware runs well. The piece needs a few dozen.

## What judges look for

On Sunday morning, you present your pitch deck to this track's judges, and they ask you to walk them through your work. Understanding and clarity count most: why your cost function works, what QAOA did, and what your results mean for a grid operator. Code counts less. See the [main README](../README.md#what-judges-look-for).

**Due Sunday 9:00 AM:** your pitch deck and your code as a ZIP ([what to submit, and where](../README.md#what-to-submit)). Have your notebook and any tools you built, run with their outputs and your IonQ job IDs. Be ready to explain:
- **Your solution:** where the sensors go, how many, and how much of the grid they see; what happens if one fails; greedy versus integer program versus QAOA; and your hardware result next to the simulator.
- **Customer and value proposition:** what a sensor costs and what a grid operator gains. A 2014 U.S. Department of Energy report, [Factors Affecting PMU Installation Costs](https://www.energy.gov/oe/articles/factors-affecting-pmu-installation-costs-october-2014), is a good starting point for costs.
- **What you learned:** where quantum honestly stands on this problem (see below).
- **What didn't work:** if something failed or you couldn't find a solution, say so clearly and explain why. That earns points.

**The notebook is a starter.** Add your own code, cells and notebooks, try a different approach, and expand as far as you like.

**Tools worth building** (they count):
- an interactive grid map where you click substations to place sensors and see what's covered;
- a "what if a sensor fails" explorer;
- a dashboard that puts greedy, the integer program and QAOA side by side;
- a visual of QAOA's answers over time, or across noise settings.

## Hardware rules

- **Tune on simulators first:** the local Aer simulator, then IonQ's free simulator (`ionq:ionq:sim:simulator`) with `runtime_options={"noise_model": "forte-1"}`. The notebook's hardware cell is set up for this.
- **Real hardware is IonQ Forte** (`ionq:ionq:qpu:forte-1`) through qBraid. Run only your final, tuned circuit.
- **Cap every hardware run at 200 shots.**
- **Send hardware runs early.** Queues can take hours, so aim for Saturday, not Sunday morning.
- **If IonQ is down or the queue isn't moving,** keep your job ID and your noisy-simulator result to show judges, and ask a qBraid mentor about IQM Garnet (`aws:iqm:qpu:garnet`) as a backup.
- Keep the hardware circuit to a few dozen two-qubit gates. The notebook prints the count.

## Stretch goals (pick any)

- **Zero-injection buses.** A zero-injection bus has no load and no generator, so the power flowing in equals the power flowing out. That lets operators work out one unseen neighbor without a sensor. IEEE 14 bus 7 is one. Use `check_placement(grid, chosen, zib=True)`. How many sensors does the rule save?
- **N-1 (every substation seen twice).** The grid stays fully visible if any one sensor fails. Use `check_placement(grid, chosen, n1=True)` and `ilp_placement(grid, twice=True)`. For QAOA, penalize each missing sighting: P × (2 − sightings) for a substation seen fewer than twice, with P > 1. (A flat penalty for "seen only once" lets invalid placements tie for best.)
- **Fixed budget.** With only *k* sensors (try k = 2 or 3 on IEEE 14), place them to see as many substations as possible. This is the second goal in NERC's guideline. How does the cost function change when you can't afford full coverage?
- **Priority weights.** Some substations matter more, such as big loads, power plants and the links between regions. Build a small priority table the way NERC's guideline suggests (a weight per application, times whether a PMU at that bus serves it), then use the weights where they can matter: with a fixed budget (k sensors, maximize the weighted substations seen), or by requiring high-priority substations to be seen twice. (A bigger penalty alone won't move the best placement when every substation can be covered.) See how the placement changes.
- **30 substations on qBraid's GPU simulator.** Load `data/ieee30.json`. The exact table of 2^30 costs no longer fits in memory, so switch to sampled shots.

## Honest quantum value

Judges reward teams that say plainly where quantum stands, with their own numbers. Answer these in your story:

- How long does your integer program take on 14 substations, and on 30? How long does QAOA take, including the hardware queue?
- How often does QAOA find a best placement, and how often does it leave a substation unseen? How does that compare with guessing at random?
- To tune QAOA, the notebook computes the cost of every placement first. What does that mean for your speed comparison?
- What would have to change, in the hardware or in the problem, for quantum to be worth it here?

Reading: Jones et al. 2020 ([arXiv 2001.04489](https://arxiv.org/abs/2001.04489)) tried a D-Wave quantum annealer on this problem for grids of several sizes. What did they find, and does your result agree?

## Links

- MATPOWER IEEE 14-bus case: <https://github.com/MATPOWER/matpower/blob/master/data/case14.m>
- MATPOWER IEEE 30-bus case: <https://github.com/MATPOWER/matpower/blob/master/data/case_ieee30.m>
- UW Power Systems Test Case Archive (the original IEEE cases): <https://labs.ece.uw.edu/pstca/>
- Background reading from TVA: NERC's *Reliability Guideline: PMU Placement and Installation* (December 2016), in [`background/`](./background/)
- TVA's original problem, in TVA's words, and what changed for this event: [`background/`](./background/)
- Data sources TVA pointed to:
  - an [IEEE overview of PMU placement](https://ieeexplore.ieee.org/document/7459248)
  - [IEEE 14-bus PMU measurements at optimal and sub-optimal locations](https://ieee-dataport.org/documents/pmu-measurements-optimal-sub-optimal-locations-ieee-14-bus-system) (IEEE DataPort)
  - the larger MATPOWER cases (57, 118 and 300 buses) in the [MATPOWER data folder](https://github.com/MATPOWER/matpower/tree/master/data)
- Jones et al. 2020, quantum annealing for PMU placement: <https://arxiv.org/abs/2001.04489>

## The qBraid Award

The qBraid Award is open to every team. It's optional; see `../4-qbraid-award/`.
