[<img src="https://qbraid-static.s3.amazonaws.com/logos/Launch_on_qBraid_white.png" width="150">](https://account.qbraid.com?gitHubUrl=https://github.com/qBraid/tn-quantum-hackathon.git)

# Tennessee Quantum Hackathon 2026

Chattanooga, November 13 to 15, 2026. Hosted by the Chattanooga Quantum Collaborative and CO.LAB. The challenges come from TVA and UTC, and qBraid is the platform partner.

Everything runs in qBraid Lab in your browser. There's nothing to install on your laptop.

## Start here (Friday evening)

1. **Join the hackathon's qBraid organization** with the invite link pinned in Discord. That's where your team's credits come from.
2. **Open this repository in qBraid Lab** with the button above, or from the Explore page in your qBraid account.
3. **Pick the kernel.** Use the qBraid SDK environment's kernel for every notebook here (Kernel > Change Kernel). The first cell installs qiskit-aer if it's missing, and stops with a message if you're on the wrong kernel.
4. **Do the warm-up** in [`0-warm-up`](./0-warm-up). It takes about 20 minutes and isn't scored. It makes sure your account, credits and hardware access all work before hacking starts.

## The tracks

Each team works on one track. Tracks are revealed and chosen on Friday at 7:00 PM. Each track takes up to 5 teams and has its own judges.

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
| Fri 7:15 PM | qBraid intro, and how judging works |
| Fri 7:30 PM | Warm-up ([`0-warm-up`](./0-warm-up)) |
| Fri 8:00 PM | Hacking starts |
| Sat 9:00 to 11:00 AM | TVA internships table |
| Sat 1:30 PM | Quantinuum technical session |
| Sat 3:30 PM | CO.LAB session: pitching your project (optional) |
| Sat 7:00 PM | qBraid tests the submission portal with teams |
| **Sun 9:00 AM** | **Hard deadline** for final project materials |
| Sun 10:30 AM | Judges come around and talk with each team |
| Sun 12:30 PM | Finalists announced |
| Sun 1:00 PM | Closing ceremony at The Landing Social House. Finalists present from 1:35 PM; winners and the qBraid Award are announced around 2:15 PM |

## What judges look for

**Everything is due Sunday at 9:00 AM.** What to submit, and where, is confirmed at kickoff, and the link goes in Discord.

Judges visit your team on Sunday morning. They look at:

- **Your understanding.** Everyone on the team should be able to explain what you did, why, and what your results mean, in plain words.
- **Your presentation:** the problem, the customer (who has this problem), your solution, and the value proposition (what it's worth to them).
- **The tools you build.** An interactive view of your grid, a dashboard that compares your quantum and classical answers, a checker that stress-tests a schedule, a visual that shows BB84 catching a spy. Each track's README has ideas.
- **Honesty.** Say plainly where quantum helps and where it doesn't yet. If something failed, or you couldn't find a solution, say so clearly and explain why. A clear account of what didn't work earns points.

Code counts less than any of these. Record every hardware job ID: it's your proof of what ran.

**Finalists** (announced Sunday 12:30 PM) present at the closing ceremony. The organizers will share the format.

## The notebooks are starters

They get you going; they aren't the whole job. Add your own code, cells and notebooks, change the approach, build tools around them, and go as far as you like. Ideas from the warm-up are fair game in any track. For example, Secure the Grid's stretch goals can reuse the warm-up's quantum random number generator, Grover's search or QAOA.

## Running on quantum hardware

- **Practice for free first.** IonQ's simulator on qBraid (`ionq:ionq:sim:simulator`) costs nothing. Its `noise_model` option adds IonQ's gate noise, which mostly shows up on circuits with many two-qubit gates. Most starter notebooks have a cell ready to go.
- **Then run on the real thing.** Swap in your track's QPU, such as IonQ Forte (`ionq:ionq:qpu:forte-1`). Real runs use credits, so tune on the simulator first and cap each run at 200 shots. Queues can take hours, so send hardware runs early: aim for Saturday, not Sunday morning.
- **If IonQ is down or its queue isn't moving,** try IQM Garnet (`aws:iqm:qpu:garnet`) or Rigetti (`rigetti:rigetti:qpu:cepheus-1-108q`). Ask a qBraid mentor before switching.
- **Quantinuum (Secure the Grid).** Open the Quantinuum page under Devices in your qBraid account, read each of Quantinuum's documents and accept their terms. You only do this once. Until you accept, Quantinuum jobs are refused. Then you run on Quantinuum through qBraid like any other device.
- **Record every job ID.** It's your proof of the run.
- **Check prices and live status** for every device in the [device catalog](https://account.qbraid.com/devices).

## Using AI

AI assistants are allowed, including qBraid's own. qBraid gives you two kinds:

- **Chat, for questions.** [AI Chat](https://account.qbraid.com/chat) in your qBraid account explains results, compares devices and decodes errors.
- **An agent, for doing the work.** In qBraid Lab, open the Launcher and click the **Claude** or **Codex** icon. The agent runs inside your Lab, so it can read your notebooks, write and run code, and build visuals.

Judges will ask you to explain your reasoning, so make sure everyone on the team understands what you submit.

## Certificates

Everyone who completes the weekend gets a qBraid completion certificate with a verification link you can post on LinkedIn. Details are at the event.

## Getting help

- **During the event:** ask a mentor, anyone from qBraid in the room, or in the hackathon Discord.
- **Overnight:** replies may be slower.
- **Docs:**
  - [qBraid docs](https://docs.qbraid.com)
  - [Getting started in qBraid Lab](https://docs.qbraid.com/v2/lab/user-guide/getting-started)
  - [Running jobs with the qBraid SDK](https://docs.qbraid.com/v2/sdk/user-guide/providers/getting-started)
