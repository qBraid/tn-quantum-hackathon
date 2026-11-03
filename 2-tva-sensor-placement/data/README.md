# Data

| File | Buses | Lines | Source |
|---|---|---|---|
| `ieee14.json` | 14 | 20 | MATPOWER [`case14.m`](https://github.com/MATPOWER/matpower/blob/master/data/case14.m) |
| `ieee30.json` | 30 | 41 | MATPOWER [`case_ieee30.m`](https://github.com/MATPOWER/matpower/blob/master/data/case_ieee30.m) |
| `ieee14_piece6.json` | 6 | 5 | cut from `ieee14.json` |

## Fields

| Field | Meaning |
|---|---|
| `buses` | bus (substation) numbers, as in the IEEE case |
| `lines` | power lines as `[from_bus, to_bus]` pairs |
| `zero_injection` | buses with no load, no shunt and no generator |
| `generator_buses` | buses with an in-service generator (power plants and synchronous condensers) |
| `load_mw` | real power load at each bus, in MW |

`check.load_grid()` reads a file and adds `neighbors`: for each bus, the set of buses one line away.

## How the files were made

The MATPOWER `.m` files were downloaded from GitHub (master branch) on Nov 3, 2026 and converted with a short parser:

- **Lines:** in-service branches only (status 1). Parallel lines between the same two buses are merged into one, since a PMU sees through either. Transformers count as lines.
- **Zero-injection buses:** load `Pd = Qd = 0`, shunt `Gs = Bs = 0`, and no in-service generator. (IEEE 14 bus 8 has no load but has a synchronous condenser, so it does not count.)
- **The 6-substation piece:** buses 2, 3, 5, 6, 10, 11 and the 5 lines among them. Lines to the rest of the grid are dropped, so it is a small grid of its own with no zero-injection buses. It was picked from all 240 connected 6-bus pieces of IEEE 14 as the one whose 1-layer QAOA circuit (one qubit per bus, X / multi-controlled phase / X penalty terms) has the fewest two-qubit gates after transpiling to `rz, sx, x, cx`: 26 CX with Qiskit 2.x (up to about 34 with Qiskit 1.4, depending on the angles).

The IEEE 30-bus file uses `case_ieee30.m`, the original IEEE case. MATPOWER's `case30.m` is a different, modified version.

## License

The IEEE 14-bus and 30-bus systems are public test cases from the University of Washington Power Systems Test Case Archive: <https://labs.ece.uw.edu/pstca/>. MATPOWER converted them from the archive's IEEE Common Data Format files.

MATPOWER's code is under the BSD 3-Clause license (Copyright (c) 1996-2025, Power Systems Engineering Research Center (PSERC) and individual contributors). Its license notes that the case files themselves are not covered by the BSD license; these two were converted from the public source above.
