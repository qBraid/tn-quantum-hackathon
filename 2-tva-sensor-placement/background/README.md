# Background: what TVA asked, and reading

TVA (the Tennessee Valley Authority) wrote two problems for this hackathon. This track is the first, PMU placement. This folder holds TVA's problem in its own words and the reading TVA shared. **Follow this track's [README](../README.md) for what to build and submit.** Use this folder to understand your customer: what TVA wants, and why.

| File | What it is |
|---|---|
| This page | TVA's problem, word for word, and what changed for this event |
| [`NERC-Reliability-Guideline-PMU-Placement.pdf`](./NERC-Reliability-Guideline-PMU-Placement.pdf) | NERC's *Reliability Guideline: PMU Placement and Installation* (December 2016), which TVA shared as background (Nov 2). The track README's [Background from TVA](../README.md#background-from-tva) sums up what it means for this problem. Useful for your value story: why utilities place PMUs, which applications they serve, and what installing one involves |

## What TVA asked

> **TVA (G&T): PMU Placement Optimization (Transmission)**
>
> **Background.** Phasor Measurement Units (PMUs) provide synchronized phasor data for state estimation and wide-area monitoring. Budget-constrained placement seeks full observability (with Zero Injection buses (ZIB) rules) and robustness to single PMU failure.
>
> **Challenge (36-hour scope).** Formulate PMU placement on a selected IEEE transmission case with:
>
> - Observability constraints (incl. zero-injection buses),
> - Optional redundancy (N-1 PMU failure),
> - Weighted "critical bus" priorities.
>
> Compare quantum-assisted placement vs. ILP/greedy baselines.
>
> **Deliverables**
>
> - PMU location set + coverage score and cost.
> - Observability proofs/metrics; robustness under single PMU failure.
> - Comparison vs. classical heuristic/ILP.
>
> **Data Needed (ready-to-use sources)**
>
> - MATPOWER IEEE cases (14/57/118/300-bus); and UW PSTCA archive.
> - Reference literature/datasets on PMU placement for IEEE systems (overview + data exemplars).

*From TVA's problem set (Aug 25). TVA's data links are in the track README's [Links](../README.md#links).*

## What's different here

TVA's problem was written for teams with power-systems and quantum experience. Most teams this weekend are new to quantum, have 36 hours, and run on hardware that handles a few dozen two-qubit gates well. So qBraid proposed a simpler version of the problem, and TVA agreed to it (Nov 2). TVA chose not to share TVA-specific grid data, so the track uses public IEEE test grids.

| TVA's original | This track |
|---|---|
| A selected IEEE case (14, 57, 118 or 300 buses) | IEEE 14 as the main grid and a 6-substation piece of it for hardware. IEEE 30, 57, 118 and 300 are stretch goals |
| Full observability, including zero-injection bus rules | Full observability is the core problem. Zero-injection buses are a stretch goal |
| Optional redundancy (N-1, one PMU fails) | A stretch goal, also part of your story ("what happens if one sensor fails") |
| Weighted "critical bus" priorities | A stretch goal: weight buses the way NERC's guideline suggests, then use the weights with a fixed sensor budget, or require key buses to be seen twice |
| Quantum-assisted placement, any method | QAOA, with a worked example. Other approaches are welcome |
| Compared with integer programming and greedy baselines | The same (milestone 2) |
| Deliverables: the PMU set with coverage and cost, observability metrics, robustness to one PMU failing, and the comparison with classical methods | Your pitch deck covers the same ground: where the sensors go and what they see, what happens if one fails, greedy vs integer program vs QAOA, and what sensors cost |
