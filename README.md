[<img src="https://qbraid-static.s3.amazonaws.com/logos/Launch_on_qBraid_white.png" width="150">](https://account.qbraid.com?gitHubUrl=https://github.com/qBraid/tn-quantum-hackathon.git)

# Tennessee Quantum Hackathon 2026

Chattanooga, November 13 to 15, 2026. Hosted by the Chattanooga Quantum Collaborative and CO.LAB, with challenges from TVA and UTC. qBraid is the platform partner.

Everything runs in qBraid Lab in your browser, so there's nothing to install.

## Start here (Friday evening)

1. **Join the hackathon's qBraid organization** with the invite link pinned in Discord. That's where your team's credits come from.
2. **Open this repository in qBraid Lab** with the button above, or from the Explore page in your qBraid account.
3. **Pick the kernel.** In Lab, install the qBraid SDK environment (one click) and use its kernel for every notebook here.
4. **Do the warm-up** in [`0-warm-up`](./0-warm-up). It takes about 20 minutes, isn't scored, and makes sure your account, credits and hardware access all work before hacking starts.

## The tracks

Each team works on one track. Tracks are revealed and chosen on Friday at 7:00 PM.

| Folder | Track | The question | Hardware | Good fit for |
|---|---|---|---|---|
| [`1-utc-secure-the-grid`](./1-utc-secure-the-grid) | **Secure the Grid** (UTC) | Catch an eavesdropper with quantum keys, size up the quantum threat to today's encryption, and design a secure grid network | IonQ or Quantinuum | Cybersecurity, CS |
| [`2-tva-sensor-placement`](./2-tva-sensor-placement) | **Grid Sensor Placement** (TVA) | What's the fewest sensors that let operators see every substation? | IonQ Forte | EE, CS |
| [`3-tva-plant-scheduling`](./3-tva-plant-scheduling) | **Power Plant Scheduling** (TVA) | Which power plants should run each hour, at the lowest cost? | IonQ Forte | EE, CS, math |
| [`4-qbraid-award`](./4-qbraid-award) | **qBraid Award** (optional, any team) | The most creative use of qBraid, on top of your track | Any | Everyone |

Every track folder has a `README.md` with the problem, milestones and what to submit, plus starter notebooks. Open the README first.

## Key times

| When | What |
|---|---|
| Fri 7:00 PM | Tracks revealed; teams choose |
| Fri 7:30 PM | Warm-up ([`0-warm-up`](./0-warm-up)) |
| Fri 8:00 PM | Hacking starts |
| **Sat 9:00 PM** | **Last hardware runs.** Queues can take hours, so send yours earlier |
| **Sun 9:00 AM** | **Hard deadline** for final project materials |
| Sun 10:30 AM | Judges visit each team |
| Sun afternoon | Closing ceremony at The Landing Social House. Six selected teams present (4 minutes each); winners and the qBraid Award are announced |

## Running on quantum hardware

- **Practice for free.** IonQ's simulator on qBraid (`ionq:ionq:sim:simulator`) costs nothing and can add realistic hardware noise. Every starter notebook has a cell ready to go.
- **Then run on the real thing.** Swap in your track's QPU, for example IonQ Forte (`ionq:ionq:qpu:forte-1`). Real runs use credits, so tune on the simulator first and cap each run at 200 shots.
- **Record every job ID.** It's your proof of the run.
- **Check prices and live status** for every device in the [device catalog](https://account.qbraid.com/devices).

## Using AI

AI assistants are allowed and encouraged, including qBraid's own [AI Chat and Agent mode](https://docs.qbraid.com/v2/ai/user-guide/overview) in your account. Keep a short note of what you asked it to do, what it got wrong and how you caught it. Judges will ask a team member to explain part of your code, so make sure you understand what you submit.

## Getting help

- Ask in the hackathon Discord, or grab a mentor or anyone from qBraid in the room. qBraid answers on Discord overnight too.
- [qBraid docs](https://docs.qbraid.com) · [Getting started in qBraid Lab](https://docs.qbraid.com/lab/user-guide/getting-started) · [Running jobs with the qBraid SDK](https://docs.qbraid.com/sdk/user-guide/providers/native)
