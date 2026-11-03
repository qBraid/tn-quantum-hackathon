# qBraid Award: most creative use of qBraid

**Optional and open to every team, in every track.** You win it with the project you're already building, and entering takes about 30 minutes at the end.

| | |
|---|---|
| **What you send** | 2 or 3 slides from the template in this folder, plus a 3 to 5 minute screen recording |
| **Where** | [The entry form](https://docs.google.com/forms/d/e/1FAIpQLSeeom5YX0jADpt1a09Xox9EUQYPtJYoaggeVy-1iX4VT3yY9g/viewform) (also pinned in Discord) |
| **When** | By **Sunday 9:00 AM**, with your final project materials |
| **Prize** | $200 in gift cards split across the winning team, plus qBraid credits for each member. Announced at the closing ceremony |
| **Judged on** | Did it run on qBraid, and how creatively did you use it? |

## Enter in 4 steps (about 30 minutes)

1. **Use qBraid in your project.** You probably already are: if your notebook runs in qBraid Lab and sends a job to a qBraid device or simulator, you qualify. Want to stand out? [Make it visual](#make-it-visual-in-one-line). That takes about 5 minutes.
2. **Fill in the slides (10 minutes).** The template is in this folder: [`qbraid-award-template.pptx`](./qbraid-award-template.pptx).
   - **Get it:** in qBraid Lab, right-click the file and choose Download.
   - **Open it:** PowerPoint, Keynote or Google Slides all work. For Google Slides, upload it to Drive, then open it with Google Slides.
   - **Fill it in:** every slide tells you what to write. The speaker notes tell you what to say in your video.
3. **Record your screen (10 minutes).** Walk through your slides, then show qBraid running. Use the [script below](#the-video-script).
4. **Fill in the [entry form](https://docs.google.com/forms/d/e/1FAIpQLSeeom5YX0jADpt1a09Xox9EUQYPtJYoaggeVy-1iX4VT3yY9g/viewform) (2 minutes).** It's also pinned in Discord. Enter:
   - team name
   - slides link
   - video link
   - one team member's qBraid email, so we can send the prize

   Set both links to "anyone with the link can view". You can edit your entry until the deadline.

## Make it visual in one line

Judges love a visual, and this gets you one fast. Run this in a notebook cell after you have results:

```python
import sys; sys.path.append("../4-qbraid-award")
from make_visual import make_visual

make_visual({"Simulator": sim_counts, "IonQ": hw_counts}, title="Our results")   # or just one counts dict
```

1. **The cell writes `visual.html`,** an animated bar chart, in the same folder as your notebook.
2. **Open it next to your notebook** in qBraid Lab's Agent Canvas panel. Run this from a Lab terminal in that folder:

   ```bash
   qbraid-canvas visual.html --title "Our results"
   ```

3. **Make it yours.** Ask your AI assistant to restyle it, add controls, animate your algorithm step by step, or turn it into a game.

For inspiration, see [Quantum Runner](https://account.qbraid.com/explore/projects/q-ready-quantum-runner-2gkzz6) on qBraid's Explore page. It's a side-scroller where a real quantum measurement decides where the gaps go.

## The slides

Keep 2 or 3 slides. Each one has instructions on it: replace the bracketed text, and delete what you don't use.

| Slide | What goes on it |
|---|---|
| 1. **qBraid features we used** | One tile for each feature you used, with a line on how. Delete the rest |
| 2. **Our best qBraid moment** | One visual (a chart, your interactive view, or a frame from your game), what it shows, and where AI helped |
| 3. **Check it** (optional) | Job IDs, links and cost |

Here's a [finished example](./qbraid-award-example.pptx) ([PDF](./qbraid-award-example.pdf)). The team is made up and the numbers are illustrative.

![Example slide: qBraid features we used](./images/example-1.png)

<details>
<summary>Example slides 2 and 3</summary>

![Example slide 2: Our best qBraid moment](./images/example-2.png)

![Example slide 3: Check it](./images/example-3.png)

</details>

## The video script

Record your screen with someone on the team talking. One take is fine, and it doesn't need editing.

| Time | Show | Say something like |
|---|---|---|
| 0:00 to 0:30 | Slide 1 | "We're [team] in the [track] track. We built [one sentence]. Here are the qBraid features we used." |
| 0:30 to 3:00 | **qBraid running:** your notebook in qBraid Lab, a job going to a device, results coming back on the Jobs page | "Here's our notebook running on qBraid. We're sending this circuit to [device]..." |
| 3:00 to 4:30 | Slide 2, or your visual running live | "This shows [result in plain words]. AI helped us [what], and we checked [what]." |
| Last 30 seconds | Slide 3, or just your face | "Next we'd try [idea]." |

**One rule:** we have to *see* it run on qBraid.

**How to record and share:**
- **Mac:** Cmd+Shift+5
- **Windows:** the Snipping Tool's record option
- **Share it:** upload it unlisted to YouTube, to Loom, or to Google Drive with "anyone with the link can view"

## Ideas

- **Make it visual (we'd love to see this).** An interactive view of your grid, an animation of QAOA converging, a live dashboard, or a game. Start from [the one-liner above](#make-it-visual-in-one-line).
- **Share it on Explore.** Put your project in a GitHub repo and submit it from qBraid's Explore page, so anyone can launch it in qBraid Lab with one click.
- **Real hardware.** Run your track's problem on IonQ or Quantinuum, and compare it with the simulator.
- **qBraid AI (encouraged).**
  - Ask [AI Chat](https://docs.qbraid.com/v2/ai/user-guide/overview) to compare devices or explain a result.
  - Run a coding agent with Agent mode.
  - Connect your own AI tool to qBraid's MCP server at `https://mcp.qbraid.com/mcp`.
- **Compare devices.** Run the same circuit on trapped-ion and superconducting hardware, and explain the difference.
- **Bigger problems.** Use qBraid's GPU simulators to go past what fits on a laptop.

**These don't count on their own:**
- signing up
- running local code in a notebook
- one "hello world" job unconnected to your project

## How we judge

qBraid staff watch every video after the deadline, with your slides open. This is separate from track judging.

1. **Did it clearly run on qBraid?** If not, the entry is out.
2. **How creatively did you use it?** Scored 1 to 5. These all push the score up:
   - a creative visualization (an interactive view, an animation or a game built on your results)
   - several qBraid features used well
   - a clever use of AI

We re-watch the top two and pick the winner.

Spending more credits doesn't help: a careful, cheap hardware run beats an expensive one.

## Quick answers

**Do we have to change our project?** No. Show how qBraid fits into what you're already building.

**We only used simulators. Can we still win?** Yes. Hardware isn't required.

**Can we use AI?** Yes, please. Say what it did and where you stepped in.

**How do I know my job ran on qBraid?** It's on the Jobs page in your qBraid account, with its job ID.

Questions? Ask anyone from qBraid at the event or in Discord.
