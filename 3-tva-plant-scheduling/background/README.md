# TVA's original problem and support material

TVA (the Tennessee Valley Authority) wrote two problems for this hackathon. This track is the second, unit commitment. The files here are TVA's, unchanged.

| File | What it is |
|---|---|
| [`TVA-Hackathon-Problem-Set.docx`](./TVA-Hackathon-Problem-Set.docx) | TVA's problem set (Aug 25). Problem 2 is this track; Problem 1 is [Grid Sensor Placement](../../2-tva-sensor-placement/) |
| [`TVA-Unit-Commitment-and-Economic-Dispatch-Overview.docx`](./TVA-Unit-Commitment-and-Economic-Dispatch-Overview.docx) | TVA's overview of how utilities decide which plants run and how much each produces (Nov 2). The [track README](../README.md#background-from-tva) sums it up |
| [`TVA-Generic-Data-for-Hackathon.md`](./TVA-Generic-Data-for-Hackathon.md) | TVA's note on which open data to use (Nov 2), as text. It recommends RTS-GMLC, which is where this track's data comes from |

The data sources TVA listed (RTS-GMLC, the NLR Reliability Test System page and MATPOWER's case files) are in the track README's [Links](../README.md#links).

## What's different here

TVA's problem was written for teams with power-systems and quantum experience. Most teams this weekend are new to quantum, have 36 hours, and run on hardware that handles a few dozen two-qubit gates well. So qBraid proposed a simpler version of the problem, and TVA agreed to it (Nov 2). TVA chose not to share TVA-specific data, so the track builds its plants from the public RTS-GMLC test system, as TVA recommended.

| TVA's original | This track |
|---|---|
| 10 to 20 units over 24 hours | 5 plants over 24 hours. 10 plants is a stretch goal |
| Thermal units and storage | Thermal plants. A battery is a stretch goal |
| Startup costs and minimum up/down times | The same, checked classically as you go hour by hour |
| Ramp limits | A stretch goal (`ramps=True` in the checker) |
| Meet load and reserve every hour | The same: demand, plus a 10% reserve |
| A hybrid solver: classical cost evaluation plus a quantum step that picks on/off schedules | The same: QAOA picks each hour's on/off choices, and classical code does the rest |
| Compared with a classical mixed-integer baseline | The same; the baseline is provided |
| Deliverables: formulation and code, a feasible schedule, cost vs the baseline with a report of broken rules, and a write-up on quantum value | The same, using the checker, in your pitch deck |

Wind and solar (scheduling against net load) is a stretch goal too.
