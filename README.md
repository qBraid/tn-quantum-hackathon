[<img src="https://qbraid-static.s3.amazonaws.com/logos/Launch_on_qBraid_white.png" width="150">](https://account.qbraid.com?gitHubUrl=https://github.com/qBraid/tn-quantum-hackathon.git)

# Tennessee Quantum Hackathon 2026

Chattanooga, November 13 to 15, 2026. Hosted by the Chattanooga Quantum Collaborative and CO.LAB. The challenges come from TVA and UTC, and qBraid is the platform partner.

Everything runs in qBraid Lab in your browser. There's nothing to install on your laptop.

## Start here (Friday evening)

1. **Join the hackathon's qBraid organization** with the invite link pinned in Discord. That's where your team's credits come from.
2. **Do the warm-up,** Friday 7:30 to 8:15 PM. It lives in its own repository, [tn-quantum-hackathon-warmup](https://github.com/qBraid/tn-quantum-hackathon-warmup) ([launch it on qBraid](https://account.qbraid.com?gitHubUrl=https://github.com/qBraid/tn-quantum-hackathon-warmup.git)). It isn't scored. It makes sure your account works and your first qBraid job runs before hacking starts.
3. **Open this repository in qBraid Lab** once track assignments are announced (8:15 PM), with the button above or from the Explore page in your qBraid account.
4. **Pick the kernel.** When you open a notebook, a **Select Kernel** box appears with *Python 3 (ipykernel)* already selected. Change it to **qBraid-SDK (v0.12.2)** and click **Select**. Do this for every notebook here. Picked the wrong one? Click the kernel name at the top right of the notebook and change it. Don't see qBraid-SDK (v0.12.2) in the list? Ask a qBraid mentor: it takes a few minutes to install. The first cell installs qiskit-aer if it's missing, stops with a message if you're on a different kernel, and ends with "Setup OK ... You're good to go" when everything's ready.
5. **Keep Lab from shutting down on you.** By default qBraid Lab asks "Session Ending Soon" every hour (click **Yes, Continue**), shuts down after 15 idle minutes, and shuts down after 2 hours. You can change all three in **Settings** at the bottom left of Lab (*Session check-ins*, *Idle timeout*, *Auto shutdown*). Your notebooks are saved either way: after a shutdown, relaunch Lab and rerun the cells.
6. **Start your pitch deck tonight.** Sketch the five slides below now and fill them in as you learn. While teammates run the notebooks, one teammate starts on the customer and value questions in your track's README.

## The tracks

Each team works on one track. The problem sets are revealed Friday at 7:15 PM, each team ranks all three, and each team's track is announced after the warm-up. Each track has its own judges.

| Folder | Track | The question | Hardware | Good fit for |
|---|---|---|---|---|
| [`1-utc-secure-the-grid`](./1-utc-secure-the-grid) | **Secure the Grid** (UTC) | Catch an eavesdropper with quantum keys, size up the quantum threat to today's encryption, and design a secure grid network | IonQ (plus Quantinuum emulators) | Cybersecurity, CS |
| [`2-tva-sensor-placement`](./2-tva-sensor-placement) | **Grid Sensor Placement** (TVA) | What's the fewest sensors that let operators see every substation? | IonQ Forte, plus Quantinuum's free emulator | EE, CS |
| [`3-tva-plant-scheduling`](./3-tva-plant-scheduling) | **Power Plant Scheduling** (TVA) | Which power plants should run each hour, at the lowest cost? | IonQ Forte, plus Quantinuum's free emulator | EE, CS, math |
| [`4-qbraid-award`](./4-qbraid-award) | **qBraid Award** (optional, any team) | The most creative use of qBraid, on top of your track | Any | Everyone |

Every track folder has a `README.md` with the problem, milestones and track-specific details, plus starter notebooks. Open the README first. Each track's `background/` folder holds the problem as UTC or TVA first wrote it, the reading they shared, and what changed for this event.

## Key times (Eastern)

| When | What |
|---|---|
| Fri 5:30 PM | Opening program, then dinner and the group photo |
| Fri 7:00 PM | The weekend, and how judging works |
| Fri 7:15 PM | Problem sets revealed; each team ranks its choices |
| Fri 7:30 PM | Warm-up and qBraid sign-up ([warm-up repo](https://github.com/qBraid/tn-quantum-hackathon-warmup)) |
| Fri 8:15 PM | Track assignments announced, and this repository opens |
| Fri 8:30 PM | Hacking starts |
| Sat 9:00 to 11:00 AM | TVA internships table |
| Sat 1:30 PM | Quantinuum technical session |
| Sat 3:30 PM | CO.LAB session: pitching your project (optional) |
| Sat 7:00 PM | qBraid checks in with teams about Sunday's submissions |
| **Sun 9:00 AM** | **Hard deadline:** pitch deck, code and the optional qBraid Award entry ([what to submit](#what-to-submit)) |
| Sun 10:30 AM | Teams present to their track's judges |
| Sun 12:20 PM | Finalists announced |
| Sun 1:00 PM | Closing ceremony at The Landing Social House: doors open at 1:00 and the program starts at 1:30. The 6 finalists present from 1:37 PM, the qBraid Award is announced at 2:10 PM, and the winners at 2:15 PM |

## What to submit

**Sunday 9:00 AM is a hard deadline.** One person submits for the whole team.

| What | Who | Where |
|---|---|---|
| **Your pitch deck** for the judges: the problem, the customer, your solution and its value | Every team | Submission link: *coming soon, and pinned in Discord* |
| **Your code**, as a ZIP of your track folder (put your own notebooks and tools in it too) | Every team | The same submission link |
| **qBraid Award entry** (optional): a link to your video and a link to your 3 slides | Any team that enters | [qBraid Award form](https://docs.google.com/forms/d/e/1FAIpQLSeeom5YX0jADpt1a09Xox9EUQYPtJYoaggeVy-1iX4VT3yY9g/viewform) ([details](./4-qbraid-award)) |

- **Make the ZIP** in a qBraid Lab terminal. First `cd` into the repo folder (run `ls` if you're not sure of its name; it's usually `tn-quantum-hackathon`), then run `python -m zipfile -c our-team.zip 2-tva-sensor-placement`, using your track's folder and your team's name. Then right-click the ZIP in the file browser and choose Download.
- **Check every link before you submit.** Set sharing to "anyone with the link can view", then open the link in a private browser window to make sure it works. Judges can't score what they can't open.
- **Bring your deck to your judging slot** on a USB stick or your laptop.

## What judges look for

On Sunday morning, each team presents its pitch deck to its track's judges. The organizers confirm how long each slot is. Build your deck around what the judges look at:

- **Your understanding.** Everyone on the team should be able to explain what you did, why, and what your results mean, in plain words.
- **Your presentation:** the problem, the customer (who has this problem), your solution, and the value proposition (what it's worth to them).
- **The tools you build.** An interactive view of your grid, a dashboard that compares your quantum and classical answers, a checker that stress-tests a schedule, a visual that shows BB84 catching a spy. Each track's README has ideas.
- **Honesty.** Say plainly where quantum helps and where it doesn't yet. If something failed, or you couldn't find a solution, say so clearly and explain why. A clear account of what didn't work earns points.

**Five slides cover it:**
1. **Problem:** what goes wrong today, and why it matters.
2. **Customer:** who has the problem, what it costs them now, and who would decide to use your solution.
3. **Solution:** what you built, with your quantum and classical results side by side.
4. **Value:** what it's worth to the customer, in numbers, with sources. Label your guesses as guesses.
5. **What we learned:** where quantum helps, where it doesn't yet, and what failed.

Code counts less than any of these: judges give it a quick look to see what you built. Keep a run record for your deck: device, job ID, shots and status for every cloud run, labeled simulator, emulator or QPU, including any that failed or are still queued. It's your proof of what ran.

**Finalists:** 6 teams, announced Sunday at 12:20 PM, each present for 4 minutes at the closing ceremony.

## The notebooks are starters

They get you going; they aren't the whole job. Add your own code, cells and notebooks, change the approach, build tools around them, and go as far as you like. Ideas from the warm-up and the other tracks are fair game. For example, Secure the Grid's stretch goals reuse the warm-up's quantum random number generator and the TVA tracks' QAOA primer.

## Running on quantum hardware

- **Practice for free first.** IonQ's simulator on qBraid (`ionq:ionq:sim:simulator`) costs nothing. Its `noise_model` option adds IonQ's gate noise, which mostly shows up on circuits with many two-qubit gates. Most starter notebooks have a cell ready to go.
- **Then run on the real thing.** Swap in your track's QPU, such as IonQ Forte (`ionq:ionq:qpu:forte-1`). Real runs use credits, so tune on the simulator first and cap each run at 200 shots. Your team's credits are meant for your track's hardware run: do that first, and ask a mentor before any other paid run. Queues can take hours, so send hardware runs early: aim for Saturday, not Sunday morning.
- **For a cheaper run, or if IonQ is down or its queue isn't moving,** try Rigetti Cepheus (`aws:rigetti:qpu:cepheus-1-108q`, about 40 credits for 200 shots) or IQM Garnet (`aws:iqm:qpu:garnet`, about 60). If `ionq:ionq:qpu:forte-1` shows as unavailable, the same IonQ Forte is also on qBraid through AWS (`aws:ionq:qpu:forte-1`, about 1,630 credits for 200 shots). Prices are from the device catalog on Nov 11. Ask a qBraid mentor before switching.
- **Quantinuum's emulator (every track; Quantinuum sponsors this event).** `quantinuum:quantinuum:sim:h2-emulator` is **free** on qBraid. It models Quantinuum's H2 trapped-ion computer, noise and readout error included, so it gives you a second, hardware-like run next to IonQ (up to 26 qubits; jobs took 1 to 4 minutes in our tests). Each notebook's qBraid cell has the lines. First open the Quantinuum page under Devices in your qBraid account and accept Quantinuum's terms: you only do this once, and until you do, Quantinuum jobs are refused. It's an emulator, so label its results that way, not as hardware. Bring your questions to Quantinuum's technical session, Saturday at 1:30 PM.
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
