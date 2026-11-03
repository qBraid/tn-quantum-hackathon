"""Checker for the TVA sensor placement track.

A PMU (sensor) at a substation (bus) sees that bus and every bus one line away.
A placement is valid when every bus is seen.

    from check import load_grid, check_placement
    grid = load_grid("data/ieee14.json")
    check_placement(grid, [1, 6, 9])            # bus numbers, not qubit numbers
    check_placement(grid, [1, 6, 9], zib=True)  # also use the zero-injection rule
    check_placement(grid, [1, 6, 9], n1=True)   # must survive losing any one sensor

Run `python check.py` for a demo.
"""
import itertools
import json
from pathlib import Path

HERE = Path(__file__).parent
_best_cache = {}


def load_grid(path):
    """Load a grid JSON file. Adds grid["neighbors"][b]: the buses one line away from bus b."""
    path = Path(path)
    if not path.exists():
        path = HERE / path  # lets you call load_grid("data/ieee14.json") from any folder
    grid = json.loads(path.read_text())
    grid["neighbors"] = {b: set() for b in grid["buses"]}
    for a, b in grid["lines"]:
        grid["neighbors"][a].add(b)
        grid["neighbors"][b].add(a)
    return grid


def bits_to_buses(grid, bits):
    """Turn a 0/1 string in qubit order (character i is qubit i, bus grid["buses"][i]) into bus numbers.
    Qiskit prints qubit 0 LAST, so reverse a Qiskit counts key first: bits_to_buses(grid, key[::-1])."""
    return [b for b, c in zip(grid["buses"], bits) if c in ("1", 1)]


def seen_buses(grid, chosen, zib=False):
    """The set of buses that the sensors in `chosen` can see.

    zib=True adds the zero-injection rule. No power enters or leaves the grid at a
    zero-injection bus, so if every bus in its group (the bus and its neighbors)
    but one is seen, Kirchhoff's current law gives the last one too.
    """
    seen = set()
    for b in chosen:
        seen |= {b} | grid["neighbors"][b]
    changed = zib
    while changed:
        changed = False
        for z in grid["zero_injection"]:
            missing = ({z} | grid["neighbors"][z]) - seen
            if len(missing) == 1:
                seen |= missing
                changed = True
    return seen


def is_valid(grid, chosen, zib=False, n1=False):
    """True when every bus is seen. With n1=True it must stay true after losing any one sensor."""
    everything = set(grid["buses"])
    if seen_buses(grid, chosen, zib) != everything:
        return False
    if n1:
        return all(seen_buses(grid, [b for b in chosen if b != lost], zib) == everything for lost in chosen)
    return True


def brute_force_best(grid, zib=False, n1=False):
    """Try every placement, smallest first. Returns (fewest sensors, list of all best placements).
    Only for grids of 20 buses or fewer."""
    buses = grid["buses"]
    if len(buses) > 20:
        raise ValueError("brute force is only for grids of 20 buses or fewer; use an integer program")
    for k in range(1, len(buses) + 1):
        best = [list(c) for c in itertools.combinations(buses, k) if is_valid(grid, c, zib, n1)]
        if best:
            return k, best
    return None, []


def check_placement(grid, chosen, zib=False, n1=False, show=True):
    """Check a placement. `chosen` is a list of bus numbers, for example [1, 6, 9].

    Returns a dict with:
      valid           every bus is seen (and, with n1=True, still seen after any one sensor fails)
      sensors         how many sensors you used
      unseen          buses no sensor sees
      coverage        share of buses seen (1.0 is full observability)
      redundancy      total sightings: for each bus, how many sensors see it, summed (higher is sturdier)
      breaks_if_lost  sensors whose failure leaves some bus unseen (None if a bus is already unseen)
      best, gap       for grids of 20 buses or fewer: the fewest sensors possible, and sensors - best
    """
    chosen = sorted(set(chosen))
    bad = [b for b in chosen if b not in grid["neighbors"]]
    if bad:
        raise ValueError(f"{bad} are not buses in {grid['name']}")
    seen = seen_buses(grid, chosen, zib)
    report = {
        "valid": is_valid(grid, chosen, zib, n1),
        "sensors": len(chosen),
        "unseen": sorted(set(grid["buses"]) - seen),
        "coverage": round(len(seen) / len(grid["buses"]), 3),
        "redundancy": sum(len(({b} | grid["neighbors"][b]) & set(chosen)) for b in grid["buses"]),
    }
    # Robustness: which single sensor failures would leave some bus unseen
    if report["unseen"]:
        report["breaks_if_lost"] = None
    else:
        report["breaks_if_lost"] = [b for b in chosen if not is_valid(grid, [c for c in chosen if c != b], zib)]
    if len(grid["buses"]) <= 20:
        key = (tuple(grid["buses"]), tuple(map(tuple, grid["lines"])), tuple(grid["zero_injection"]), zib, n1)
        if key not in _best_cache:
            _best_cache[key] = brute_force_best(grid, zib, n1)[0]
        report["best"] = _best_cache[key]
        report["gap"] = report["sensors"] - report["best"]
    if show:
        _print_report(grid, chosen, report, zib, n1)
    return report


def _print_report(grid, chosen, r, zib, n1):
    rules = " + ".join(["see neighbors"] + (["zero-injection rule"] if zib else []) + (["N-1"] if n1 else []))
    print(f"{grid['name']} | rules: {rules} | sensors at {chosen}")
    if r["valid"]:
        print(f"  VALID with {r['sensors']} sensors, redundancy {r['redundancy']}")
        weak = r["breaks_if_lost"]
        print(f"  if the sensor at any of {weak} fails, some bus goes unseen" if weak else "  survives any single sensor failure")
    elif r["unseen"]:
        print(f"  NOT VALID: buses {r['unseen']} are unseen (coverage {r['coverage']:.0%})")
    else:
        print(f"  NOT VALID under N-1: losing the sensor at any of {r['breaks_if_lost']} leaves a bus unseen")
    if "gap" in r and r["valid"]:
        print("  that is the fewest possible" if r["gap"] == 0 else f"  {r['gap']} more than the fewest possible")


if __name__ == "__main__":
    piece = load_grid("data/ieee14_piece6.json")
    grid = load_grid("data/ieee14.json")
    print("Piece buses:", piece["buses"], "lines:", piece["lines"], "\n")
    check_placement(piece, [3, 6])
    check_placement(piece, [3, 6, 10])
    print()
    plants = grid["generator_buses"]  # a first guess: a sensor at every power plant
    check_placement(grid, plants)
    check_placement(grid, plants, zib=True)  # the zero-injection rule at bus 7 recovers bus 9
    check_placement(grid, plants + [9], n1=True)
