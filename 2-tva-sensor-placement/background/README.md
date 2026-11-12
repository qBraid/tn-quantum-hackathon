# TVA's original problem and support material

TVA (the Tennessee Valley Authority) wrote two problems for this hackathon. This track is the first, PMU placement. The files here are TVA's, unchanged.

| File | What it is |
|---|---|
| [`TVA-Hackathon-Problem-Set.docx`](./TVA-Hackathon-Problem-Set.docx) | TVA's problem set (Aug 25). Problem 1 is this track; Problem 2 is [Power Plant Scheduling](../../3-tva-plant-scheduling/) |
| [`NERC-Reliability-Guideline-PMU-Placement.pdf`](./NERC-Reliability-Guideline-PMU-Placement.pdf) | NERC's *Reliability Guideline: PMU Placement and Installation* (December 2016), which TVA shared as background (Nov 2). The [track README](../README.md#background-from-tva) sums up what it means for this problem |

The data sources TVA listed (MATPOWER, the UW Power Systems Test Case Archive, and the IEEE PMU-placement paper and dataset) are in the track README's [Links](../README.md#links).

## What's different here

TVA's problem was written for teams with power-systems and quantum experience. Most teams this weekend are new to quantum, have 36 hours, and run on hardware that handles a few dozen two-qubit gates well. So qBraid proposed a simpler version of the problem, and TVA agreed to it (Nov 2). TVA chose not to share TVA-specific grid data, so the track uses public IEEE test grids.

| TVA's original | This track |
|---|---|
| A selected IEEE case (14, 57, 118 or 300 buses) | IEEE 14 as the main grid, a 6-substation piece of it for hardware, and IEEE 30 as a stretch goal |
| Full observability, including zero-injection bus rules | Full observability is the core problem. Zero-injection buses are a stretch goal |
| Optional redundancy (N-1, one PMU fails) | A stretch goal, also part of your story ("what happens if one sensor fails") |
| Weighted "critical bus" priorities | A stretch goal (priority weights, built the way NERC's guideline suggests) |
| Quantum-assisted placement, any method | QAOA, with a worked example. Other approaches are welcome |
| Compared with integer programming and greedy baselines | The same (milestone 2) |
| Deliverables: the PMU set with coverage and cost, observability metrics, robustness to one PMU failing, and the comparison with classical methods | Your pitch deck covers the same ground: where the sensors go and what they see, what happens if one fails, greedy vs integer program vs QAOA, and what sensors cost |
