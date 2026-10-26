"""Draw figure 1 (five layers and two cross-cutting concerns) as landscape/figures/layers.svg.

Run from the repository root: python3 landscape/figures/src/layers.py
"""

FG, MUTED, RULE, ACCENT, CARD = "#1d2330", "#5b6372", "#e3e0d8", "#c4511a", "#ffffff"
FONT = 'system-ui, -apple-system, "Segoe UI", sans-serif'

# Top to bottom: number, name, question (two lines).
LAYERS = [
    (5, "Communication", "How can others read, cite", "and use the result?"),
    (4, "Evidence", "What has been checked,", "on which claim, and by whom?"),
    (3, "Research", "What has been tried,", "and how can work continue?"),
    (2, "Statements", "What is claimed, and how", "does it connect to other claims?"),
    (1, "Sources", "Which problems, results", "and examples can we draw on?"),
]
CROSS = [("Provenance", "who or what produced each piece"), ("Governance", "who decides, who pays")]

W_STACK, H_LAYER, GAP, W_CROSS = 272, 70, 8, 36
H = len(LAYERS) * H_LAYER + (len(LAYERS) - 1) * GAP
W = W_STACK + len(CROSS) * (GAP + W_CROSS)


parts = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-1 -1 {W + 2} {H + 2}" '
         f'width="{W + 2}" height="{H + 2}" font-family=\'{FONT}\'>']
for i, (n, name, q1, q2) in enumerate(LAYERS):
    y = i * (H_LAYER + GAP)
    parts.append(f'<rect x="0" y="{y}" width="{W_STACK}" height="{H_LAYER}" rx="6" fill="{CARD}" '
                 f'stroke="{RULE}" stroke-width="1"/>')
    parts.append(f'<text x="12" y="{y + 22}" font-size="14" font-weight="700" fill="{ACCENT}">{n}</text>')
    parts.append(f'<text x="28" y="{y + 22}" font-size="14" font-weight="700" fill="{FG}">{name}</text>')
    parts.append(f'<text x="28" y="{y + 41}" font-size="12.5" fill="{MUTED}">{q1}</text>')
    parts.append(f'<text x="28" y="{y + 58}" font-size="12.5" fill="{MUTED}">{q2}</text>')
for j, (name, gloss) in enumerate(CROSS):
    x = W_STACK + GAP + j * (GAP + W_CROSS)
    parts.append(f'<rect x="{x}" y="0" width="{W_CROSS}" height="{H}" rx="6" fill="{CARD}" stroke="{RULE}"/>')
    cx, cy = x + W_CROSS / 2 + 5, H / 2
    parts.append(f'<text transform="translate({cx} {cy}) rotate(-90)" text-anchor="middle" font-size="13" '
                 f'fill="{MUTED}"><tspan font-weight="700" fill="{FG}">{name}</tspan> · {gloss}</text>')
parts.append("</svg>\n")
open("landscape/figures/layers.svg", "w").write("".join(parts))
