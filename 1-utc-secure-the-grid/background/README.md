# UTC's original problem set

These are the documents UTC (the University of Tennessee at Chattanooga) wrote for this hackathon, unchanged. They're here for reference. **Work in the notebooks one folder up**, not these: those fix bugs found in testing.

| File | What it is |
|---|---|
| [`UTC-Hackathon-Problem-Set.pdf`](./UTC-Hackathon-Problem-Set.pdf) | UTC's problem set (Aug 25): six problems, each with numbered Parts |
| [`UTC-Starter-Guide.docx`](./UTC-Starter-Guide.docx) | UTC's note to the organizers describing its six starter notebooks |
| [`notebooks/`](./notebooks/) | UTC's six starter notebooks (Oct 24 to 26), plus UTC's second version of Problem 4 (`_FIXED`) |

## Where each UTC problem went

UTC's set let each team pick one or two problems by level. For this event, Problems 3, 4 and 6 form one track, and the rest moved elsewhere.

| UTC problem | Where it is now |
|---|---|
| 1. Find the Fault (Grover's search) | This track, Step 2, Part 5: [`2b_grover_symmetric_keys.ipynb`](../2b_grover_symmetric_keys.ipynb) |
| 2. Islanding the Grid (QAOA on Max-Cut) | The worked example [`qaoa_primer.ipynb`](../../2-tva-sensor-placement/qaoa_primer.ipynb) in both TVA tracks |
| 3. Catch the Eavesdropper (BB84) | This track, Step 1: [`1_bb84_eavesdropper.ipynb`](../1_bb84_eavesdropper.ipynb) |
| 4. Harvest Now, Decrypt Later (Shor's algorithm and post-quantum cryptography) | This track, Step 2, Parts 1 to 4: [`2_shor_harvest_now.ipynb`](../2_shor_harvest_now.ipynb) |
| 5. Randomness You Can Trust (quantum random numbers) | Friday's warm-up: [tn-quantum-hackathon-warmup](https://github.com/qBraid/tn-quantum-hackathon-warmup) |
| 6. Design the Secure Grid Backbone (capstone) | This track, Step 3: [`3_secure_grid_link.ipynb`](../3_secure_grid_link.ipynb) |

## What's different here

The Parts of Problems 3, 4 and 6 are UTC's, almost word for word. The changes:

- **Problem 1 is told as a search for a secret key** (Grover's search against symmetric encryption), so it fits this track's security story. UTC told it as finding a faulted section of power line. The code is the same: you still write the oracle and the diffusion step. N = 16 and the hardware run are optional, and the speedup plot is replaced by a question about symmetric key length.
- **Problem 3 sends 200 qubits instead of 100**, so the error rate comes out steadier, and the hardware run is packed into one job.
- **Problem 4 factors 15** (UTC offered 15 or 21), and the notebook lists qBraid's devices for you.
- **Problems 2 and 5 aren't scored.** Problem 2 is a worked example for the TVA tracks, and its GPU scale-up is optional. Problem 5 is the warm-up, with nothing to submit.
- **Hardware:** use your team's qBraid credits. The problem set's step "link your Open Quantum account" doesn't apply. See [Hardware](../README.md#hardware).
- **What you submit:** one pitch deck and a ZIP of your code per team, with your written answers in a `WRITEUP.md` labeled by Step and Part. UTC's set asked for a written response and a 5-slide presentation per problem. See [what to submit](../../README.md#what-to-submit).
- **Problem 4's notebook:** UTC's first version applies the same multiplication at every step, so its measured phases come out wrong and it rarely finds 3 × 5. UTC's `_FIXED` version works, and the track's notebook is built from it. The track's version also makes the circuit multiply by 7, as its name says (UTC's multiplies by 13, which has the same period, so it still factors 15).
