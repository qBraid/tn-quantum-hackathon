# Secure the Grid (UTC)

**A utility's network has to stay secret, today and after large quantum computers arrive. Show how quantum physics can catch an eavesdropper, size up the quantum threat to today's encryption, and design the network that handles both.**

A city-scale utility like Chattanooga's EPB runs a fiber network linking its substations and control centers. Two threats hang over it. Someone could be listening on a link right now. And an attacker could record encrypted traffic today and decrypt it years from now on a quantum computer. This track takes you through both, one step at a time, and ends with your design for the whole network.

These problems come from UTC (Problems 3, 4 and 6 of its problem set).

## Start here

1. Open [`1_bb84_eavesdropper.ipynb`](./1_bb84_eavesdropper.ipynb) with the qBraid SDK environment's kernel and run the cells.
2. Fill in the `TODO`s. Each one has a hint.
3. Do the steps in order. Each one feeds the next.

| Step | Notebook | The question | Time |
|---|---|---|---|
| 1. Catch the eavesdropper | [`1_bb84_eavesdropper.ipynb`](./1_bb84_eavesdropper.ipynb) | Can two substations share a secret key, and spot a spy by the errors they cause? | 4 to 5 h |
| 2. Size up the threat | [`2_shor_harvest_now.ipynb`](./2_shor_harvest_now.ipynb) | How real and how urgent is "harvest now, decrypt later," and what should the utility fix first? | 4 to 5 h |
| 3. Design the network | [`3_secure_grid_link.ipynb`](./3_secure_grid_link.ipynb) | Where should the network use quantum keys, and where post-quantum cryptography? | 5 to 6 h |

## Step 1: Catch the eavesdropper (BB84)

Two substations need a shared secret key to encrypt the data between them. Quantum key distribution (QKD) lets them make one in a way that reveals any eavesdropper. The best-known QKD protocol, BB84, doesn't rely on hard math. It relies on physics: measuring a quantum system disturbs it, and the disturbance shows up as errors.

- **Part 1. Shared key, no eavesdropper.** Run BB84 on the simulator and show both parties end up with matching keys, with near-zero error.
- **Part 2. Add the eavesdropper.** Add an eavesdropper who intercepts each qubit and resends it. Report the error rate (QBER) with and without the eavesdropper, and show the jump.
- **Part 3. Hardware and thresholds.** Run the protocol on real hardware and report the error rate from hardware noise alone. The notebook packs 16 rounds into one circuit, so this is **one job**, not one job per qubit. Then answer in a few sentences: how should a utility set a threshold that separates a real eavesdropper from normal line noise?
- **Part 4. Why physics wins (written).** In one short paragraph, explain why BB84's security comes from physics, and what classical key exchange can't match.
- **Stretch.** Run your protocol on two different simulator backends through qBraid and show the error rate is consistent.

## Step 2: Size up the threat (Shor's algorithm and post-quantum cryptography)

Much of today's security, including the grid's, relies on RSA and elliptic-curve cryptography. A large enough quantum computer running Shor's algorithm could break both. That makes "harvest now, decrypt later" a real risk for long-lived infrastructure: record the traffic today, decrypt it later.

- **Part 1. Shor demo.** Run Shor's algorithm to factor 15 on the simulator. Report the factors, plus a sentence or two on what Shor's algorithm threatens.
- **Part 2. Hardware gap.** The notebook lists qBraid's real quantum computers. Record their qubit counts, estimate the order of magnitude of qubits needed to break RSA-2048, and state how big the gap is today.
- **Part 3. Exposure map (written).** List the utility systems that rely on RSA or elliptic-curve cryptography, and so are exposed. Consider SCADA control links, remote-access VPNs and firmware-update signing.
- **Part 4. Migration plan (written).** Propose a move to NIST's post-quantum standards: [ML-KEM (FIPS 203)](https://csrc.nist.gov/pubs/fips/203/final) for key exchange and [ML-DSA (FIPS 204)](https://csrc.nist.gov/pubs/fips/204/final) for signatures. Rank what the utility should fix first, and explain why.
- **Stretch.** Identify systems that are hard to patch, such as field devices with long lifespans, and explain why they need attention now.

## Step 3: Design the network (capstone)

Now put it together. Securing a metro-scale grid network takes more than one tool. Some links may use QKD, others post-quantum cryptography (PQC). The right mix depends on distance, cost, the number of sites and hard practical limits.

- **Part 1. Architecture.** A diagram and a written rationale showing where you use QKD and where PQC, and why. Address distance limits, the number of substations, the "trusted node" problem on long QKD links, and timing synchronization across sites.
- **Part 2. Assumptions and tradeoffs.** List your key assumptions and tradeoffs. Back up every hardware limit with real numbers from qBraid's device list, not guesses.
- **Part 3. Working prototype.** Build and run one link on qBraid: reuse your BB84 from Step 1, or finish the teleportation link in the notebook.
- **Part 4. Rollout plan.** A phased plan: what the utility deploys first, next and later, and why.
- **Stretch.** A short cost-versus-security argument aimed at the utility's board.

## Hardware

| Device | qBraid ID | Notes |
|---|---|---|
| IonQ simulator | `ionq:ionq:sim:simulator` | **Free.** Use `noise_model="aria-1"` to mimic hardware |
| IonQ Forte | `ionq:ionq:qpu:forte-1` | Real QPU. Uses credits |
| Quantinuum | Posted in Discord once access opens | You'll get an invite to Quantinuum's Nexus portal. Accept it and its terms before Saturday, then run through qBraid |
| IQM Garnet | `aws:iqm:qpu:garnet` | Backup if IonQ is down or its queue isn't moving. Ask a qBraid mentor first |

Rules:
- Get it right on a simulator first.
- Cap each hardware run at 200 shots, and plan on one hardware run for each Part that asks for one (UTC's guidance). Simulators are free and unlimited.
- Last hardware runs: **Saturday 9:00 PM**.
- Write down every job ID.

## What to submit (by Sunday 9:00 AM)

1. **Your notebooks**, with code that runs and your hardware job IDs.
2. **Written answers** to each Part. Label them by step and Part (for example, "Step 1, Part 3") so judges can follow along.
Judges visit your team on Sunday morning, and selected teams present a 5-slide deck at the closing ceremony (see the [main README](../README.md#judging-and-the-finalist-deck)). In that deck, your network design from Step 3 is the Solution, and the utility is the Customer.

Judges look for three things: does it work, do you understand why it works, and can you explain it to someone who isn't an expert. A design that uses only post-quantum cryptography can score just as well as one with QKD everywhere, if you justify it.

Also open to your team: the [qBraid Award](../4-qbraid-award) for the most creative use of qBraid.

## Links

- [qBraid device catalog](https://account.qbraid.com/devices) (qubit counts, prices, status)
- [NIST post-quantum cryptography](https://csrc.nist.gov/projects/post-quantum-cryptography)
- [EPB Quantum Network](https://epbquantum.com) (Chattanooga's commercial quantum network)
