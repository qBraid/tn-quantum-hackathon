# Warm-up: setup check

**Friday, 7:30 PM. About 20 minutes. Not scored.**

The point is to hit any login, kernel or credit problem now, not at midnight. These notebooks come from UTC's problem set.

## Do this first (every team)

1. Open [`qrng_randomness.ipynb`](./qrng_randomness.ipynb) with the qBraid SDK environment's kernel.
2. Fill in the one `TODO` (two lines) and run every cell down to the hardware cell.
3. Run the hardware cell as written. It sends your circuit to IonQ's **free** simulator on qBraid and prints a **job ID**.
4. Open the **Jobs** page in your qBraid account and find that job. If it's there, your account works.

Stuck on any step? Flag a qBraid mentor right away.

## If you have time

| Notebook | What it is | Time |
|---|---|---|
| [`qrng_randomness.ipynb`](./qrng_randomness.ipynb) | **Randomness You Can Trust:** a quantum random number generator compared with software randomness | 15 min for the setup check |
| [`grover_find_the_fault.ipynb`](./grover_find_the_fault.ipynb) | **Find the Fault:** Grover's search finds one faulted node among N in about √N steps | 30 to 60 min |
| [`qaoa_islanding.ipynb`](./qaoa_islanding.ipynb) | **Islanding the Grid:** QAOA splits a grid in two (Max-Cut). **Recommended before either TVA track**, which both use QAOA | About 1 hour |

## Using AI

Now's a good time to set up the AI helper you'll use this weekend. qBraid's [AI Chat](https://docs.qbraid.com/v2/ai/user-guide/overview) is built into your account. Try asking it to explain the QRNG circuit, or why the simulator's bits aren't truly random.
