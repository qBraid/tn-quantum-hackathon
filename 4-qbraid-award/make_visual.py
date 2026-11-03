"""Turn your measurement results into an animated, shareable chart in one line.

In a notebook cell:

    from make_visual import make_visual
    make_visual({"Simulator": sim_counts, "IonQ Forte": qpu_counts}, title="Our results")

That writes visual.html: one self-contained file (no internet needed) with animated
bars, which you can open in qBraid Lab's Agent Canvas panel from a terminal:

    qbraid-canvas visual.html --title "Our results"

You can pass one counts dict, or several labeled ones to compare (simulator vs hardware,
one device vs another). Then make it yours: ask your AI assistant to restyle it, add
controls, or turn it into a game.
"""

import html
import sys

PALETTE = ["#6c3ce1", "#e0457b", "#2bb3a3", "#f2a33a"]


def make_visual(results, title="Our results", path="visual.html", top=16):
    """Write an animated bar chart of measurement counts to a self-contained HTML file.

    results: a counts dict like {"010": 51, "101": 49}, or a dict of labeled counts dicts
             like {"Simulator": {...}, "Hardware": {...}}.
    top:     how many of the most frequent outcomes to show.
    """
    if results and all(isinstance(v, (int, float)) for v in results.values()):
        results = {"Results": results}
    series = {name: {k: v / max(sum(c.values()), 1) for k, v in c.items()} for name, c in results.items()}
    first = next(iter(series.values()))
    keys = sorted({k for s in series.values() for k in s}, key=lambda k: -first.get(k, 0))[:top]
    colors = {name: PALETTE[i % len(PALETTE)] for i, name in enumerate(series)}
    peak = max([v for s in series.values() for v in s.values()] or [1])
    legend = "".join(f'<span style="--c:{colors[n]}">{html.escape(n)}</span>' for n in series)
    groups = []
    for k in keys:
        bars = "".join(
            f'<div class="bar" style="--c:{colors[n]};height:{100 * s.get(k, 0) / peak:.1f}%" '
            f'data-h="{100 * s.get(k, 0) / peak:.1f}%" title="{html.escape(n)}: {100 * s.get(k, 0):.1f}% of shots"></div>'
            for n, s in series.items())
        groups.append(f'<div class="group"><div class="bars">{bars}</div><div class="label">{html.escape(k)}</div></div>')
    page = (TEMPLATE.replace("__TITLE__", html.escape(title))
            .replace("__LEGEND__", legend).replace("__GROUPS__", "".join(groups)))
    with open(path, "w") as f:
        f.write(page)
    print(f"Wrote {path}. Open it in qBraid Lab's Canvas panel from a terminal:")
    print(f'  qbraid-canvas {path} --title "{title}"')
    return path


TEMPLATE = """<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>__TITLE__</title>
<style>
  body { margin: 0; font-family: -apple-system, Segoe UI, Roboto, Arial, sans-serif; background: #f6f4fd; color: #1b1530; }
  main { max-width: 900px; margin: 0 auto; padding: 24px 16px; }
  h1 { font-size: 26px; margin: 0 0 4px; }
  p.sub { margin: 0 0 18px; color: #6b6585; }
  .legend { display: flex; gap: 16px; flex-wrap: wrap; margin-bottom: 14px; font-size: 14px; }
  .legend span::before { content: ""; display: inline-block; width: 12px; height: 12px; border-radius: 3px; margin-right: 6px; background: var(--c); vertical-align: -1px; }
  .chart { display: flex; align-items: flex-end; justify-content: space-evenly; gap: 10px; height: 320px; padding: 12px; background: #fff; border-radius: 14px; overflow-x: auto; }
  .group { display: flex; flex-direction: column; align-items: center; min-width: 38px; height: 100%; justify-content: flex-end; }
  .bars { display: flex; align-items: flex-end; gap: 3px; height: calc(100% - 22px); }
  .bar { width: 14px; border-radius: 4px 4px 0 0; background: var(--c); transition: height 0.9s cubic-bezier(.2,.8,.2,1); }
  .label { font: 12px ui-monospace, Menlo, monospace; margin-top: 6px; color: #6b6585; }
  button { margin-top: 14px; padding: 8px 14px; border: 0; border-radius: 8px; background: #6c3ce1; color: #fff; font-size: 14px; cursor: pointer; }
</style></head>
<body><main>
  <h1>__TITLE__</h1>
  <p class="sub">Share of shots for each measured outcome. Hover a bar for its value.</p>
  <div class="legend">__LEGEND__</div>
  <div class="chart">__GROUPS__</div>
  <button id="replay">Replay</button>
</main>
<script>
// The chart is already drawn above; this only animates the bars growing in.
const bars = [...document.querySelectorAll(".bar")];
function play() {
  bars.forEach(b => b.style.height = "0%");
  setTimeout(() => bars.forEach((b, j) => setTimeout(() => b.style.height = b.dataset.h, 25 * j)), 60);
}
document.getElementById("replay").onclick = play; play();
</script></body></html>
"""

if __name__ == "__main__":
    demo = {"Simulator": {"00": 498, "11": 502}, "Hardware": {"00": 471, "11": 489, "01": 22, "10": 18}}
    make_visual(demo, title="Bell state: simulator vs hardware", path=sys.argv[1] if len(sys.argv) > 1 else "visual.html")
