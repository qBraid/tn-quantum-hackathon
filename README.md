[<img src="https://qbraid-static.s3.amazonaws.com/logos/Launch_on_qBraid_white.png" width="150">](https://account.qbraid.com?gitHubUrl=https://github.com/qBraid/tn-quantum-hackathon.git)

# Tennessee Quantum Hackathon 2026

Chattanooga, November 13 to 15, 2026. Hosted by the Chattanooga Quantum Collaborative and CO.LAB. The challenges come from TVA and UTC, and qBraid is the platform partner.

Everything runs in qBraid Lab in your browser. There's nothing to install.

## Start here (Friday evening)

1. **Join the hackathon's qBraid organization** with the invite link pinned in Discord. That's where your team's credits come from.
2. **Open this repository in qBraid Lab** with the button above, or from the Explore page in your qBraid account.
3. **Pick the kernel.** Use the qBraid SDK environment's kernel for every notebook here. The first cell of each notebook installs anything that's missing.
4. **Do the warm-up** in [`0-warm-up`](./0-warm-up). It takes about 20 minutes and isn't scored. It makes sure your account, credits and hardware access all work before hacking starts.

## The tracks

Each team works on one track. Tracks are revealed and chosen on Friday at 7:00 PM, and each track has its own judges.

| Folder | Track | The question | Hardware | Good fit for |
|---|---|---|---|---|
| [`1-utc-secure-the-grid`](./1-utc-secure-the-grid) | **Secure the Grid** (UTC) | Catch an eavesdropper with quantum keys, size up the quantum threat to today's encryption, and design a secure grid network | IonQ or Quantinuum | Cybersecurity, CS |
| [`2-tva-sensor-placement`](./2-tva-sensor-placement) | **Grid Sensor Placement** (TVA) | What's the fewest sensors that let operators see every substation? | IonQ Forte | EE, CS |
| [`3-tva-plant-scheduling`](./3-tva-plant-scheduling) | **Power Plant Scheduling** (TVA) | Which power plants should run each hour, at the lowest cost? | IonQ Forte | EE, CS, math |
| [`4-qbraid-award`](./4-qbraid-award) | **qBraid Award** (optional, any team) | The most creative use of qBraid, on top of your track | Any | Everyone |

Every track folder has a `README.md` with the problem, milestones and track-specific details, plus starter notebooks. Open the README first.

## Key times (Eastern)

| When | What |
|---|---|
| Fri 7:00 PM | Tracks revealed; teams choose |
| Fri 7:30 PM | Warm-up ([`0-warm-up`](./0-warm-up)) |
| Fri 8:00 PM | Hacking starts |
| **Sat 9:00 PM** | **Last hardware runs.** Queues can take hours, so send yours earlier |
| **Sun 9:00 AM** | **Hard deadline** for final project materials |
| Sun 10:30 AM | Judges come around and talk with each team |
| Sun 12:30 PM | Finalists announced; they build a 5-slide deck |
| Sun afternoon | Closing ceremony at The Landing Social House. Selected teams present (4 minutes each), and winners and the qBraid Award are announced |

## What every team submits (by Sunday 9:00 AM)

1. **Your notebooks**, run top to bottom, with every hardware job ID recorded in them.
2. **Anything extra your track asks for.** For example, Secure the Grid asks for written answers to each Part.

Submit through the submission portal (details in Discord).

## Judging and the finalist deck

- **Judges visit your team (Sunday 10:30 AM to noon).** Be ready to walk them through your work. Everyone on the team should be able to explain it.
- **If your team is selected (announced at 12:30 PM),** you build a 5-slide deck and present it for 4 minutes at the closing ceremony. The slides are: Problem, Customer, Solution, Value Proposition, What We Learned. Aim for about half technical and half business.
- **Plan the deck as you go.** Your track's README lists what your Solution slide should show.

## Running on quantum hardware

- **Practice for free first.** IonQ's simulator on qBraid (`ionq:ionq:sim:simulator`) costs nothing and can add realistic hardware noise. Every starter notebook has a cell ready to go.
- **Then run on the real thing.** Swap in your track's QPU, such as IonQ Forte (`ionq:ionq:qpu:forte-1`). Real runs use credits, so tune on the simulator first and cap each run at 200 shots.
- **If IonQ is down or its queue isn't moving,** try IQM Garnet (`aws:iqm:qpu:garnet`) or Rigetti (`rigetti:rigetti:qpu:cepheus-1-108q`). Ask a qBraid mentor before switching.
- **Quantinuum (Secure the Grid).** You'll get an invite to Quantinuum's Nexus portal. Accept it and its terms before Saturday, then you run through qBraid.
- **Record every job ID.** It's your proof of the run.
- **Check prices and live status** for every device in the [device catalog](https://account.qbraid.com/devices).

## Using AI

AI assistants are allowed, including qBraid's own [AI Chat and Agent mode](https://docs.qbraid.com/v2/ai/user-guide/overview) in your account. Judges will ask you to explain your reasoning, so make sure everyone on the team understands what you submit.

## Certificates

Everyone who completes the weekend gets a qBraid completion certificate with a verification link you can post on LinkedIn. Details are at the event.

## Getting help

- **During the event:** ask a mentor, anyone from qBraid in the room, or in the hackathon Discord.
- **Overnight:** replies may be slower.
- **Docs:**
  - [qBraid docs](https://docs.qbraid.com)
  - [Getting started in qBraid Lab](https://docs.qbraid.com/lab/user-guide/getting-started)
  - [Running jobs with the qBraid SDK](https://docs.qbraid.com/sdk/user-guide/providers/native)
