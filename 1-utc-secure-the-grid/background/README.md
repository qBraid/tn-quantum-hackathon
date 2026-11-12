# Background: UTC's original problem set

UTC (the University of Tennessee at Chattanooga) wrote these problems for this hackathon. The problem set is here so you can see what UTC first asked. **Follow this track's [README](../README.md) for what to build and submit**, and work in its notebooks.

| File | What it is |
|---|---|
| [`UTC-Hackathon-Problem-Set.pdf`](./UTC-Hackathon-Problem-Set.pdf) | UTC's problem set (Aug 25): six problems, each with numbered Parts |

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

- **Problem 1 is told as a search for a secret key** (Grover's search against symmetric encryption), so it fits this track's security story. UTC told it as finding a faulted section of power line. You still write the oracle and the diffusion step. N = 16 and the hardware run are optional, and the speedup plot is replaced by a question about symmetric key length.
- **Problem 3 sends 200 qubits instead of 100**, so the error rate comes out steadier, and the hardware run is packed into one job.
- **Problem 4 factors 15** (UTC offered 15 or 21), and the notebook lists qBraid's devices for you.
- **Problems 2 and 5 aren't scored.** Problem 2 is a worked example for the TVA tracks, and its GPU scale-up is optional. Problem 5 is the warm-up, with nothing to submit.
- **Hardware:** use your team's qBraid credits. The problem set's step "link your Open Quantum account" doesn't apply. See [Hardware](../README.md#hardware).
- **What you submit:** one pitch deck and a ZIP of your code per team, with your written answers in a `WRITEUP.md` labeled by Step and Part. UTC's set asked for a written response and a 5-slide presentation per problem. See [what to submit](../../README.md#what-to-submit).
