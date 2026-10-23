"""Draw figure 1 (five layers and two cross-cutting concerns) as figures/layers.svg.

Run from the repository root: python3 figures/src/layers.py
"""

FG, MUTED, RULE, ACCENT, CARD = "#1d2330", "#5b6372", "#e3e0d8", "#c4511a", "#ffffff"
FONT = 'system-ui, -apple-system, "Segoe UI", sans-serif'

# Top to bottom: number, name, question (two lines), state, how full its dot is.
LAYERS = [
    (5, "Views and venues", "How does a person read it, cite it,", "build on it?", "emerging", 0.25),
    (4, "Evidence", "Why should anyone believe it,", "and is it new?", "uneven", 0.5),
    (3, "Work", "What has been tried, what failed,", "and why?", "young, fragmented", 0.5),
    (2, "Statements and identity", "What exactly is claimed? Is it the", "same claim as that one?", "partial", 0.5),
    (1, "Sources and objects", "What is known, what is asked,", "where is it written?", "well served", 1.0),
]
CROSS = [("Provenance", "who or what produced each piece"), ("Governance", "who decides, who pays")]

W_STACK, H_LAYER, GAP, W_CROSS = 272, 70, 8, 36
H = len(LAYERS) * H_LAYER + (len(LAYERS) - 1) * GAP
W = W_STACK + len(CROSS) * (GAP + W_CROSS)


def dot(cx, cy, fill, colour, r=5):
    """A state dot: the filled share (1, 1/2, 1/4, 0) carries the state, not only the colour."""
    out = [f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{colour}" stroke-width="1.5"/>']
    if fill == 1:
        out.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{colour}"/>')
    elif fill == 0.5:
        out.append(f'<path d="M{cx} {cy - r}A{r} {r} 0 0 0 {cx} {cy + r}Z" fill="{colour}"/>')
    elif fill == 0.25:
        out.append(f'<path d="M{cx} {cy}V{cy - r}A{r} {r} 0 0 1 {cx + r} {cy}Z" fill="{colour}"/>')
    return "".join(out)


parts = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-1 -1 {W + 2} {H + 2}" '
         f'width="{W + 2}" height="{H + 2}" font-family=\'{FONT}\'>']
for i, (n, name, q1, q2, state, fill) in enumerate(LAYERS):
    y = i * (H_LAYER + GAP)
    work = n == 3
    parts.append(f'<rect x="0" y="{y}" width="{W_STACK}" height="{H_LAYER}" rx="6" fill="{CARD}" '
                 f'stroke="{ACCENT if work else RULE}" stroke-width="{2 if work else 1}"/>')
    parts.append(f'<text x="12" y="{y + 22}" font-size="14" font-weight="700" fill="{ACCENT}">{n}</text>')
    parts.append(f'<text x="28" y="{y + 22}" font-size="14" font-weight="700" fill="{FG}">{name}</text>')
    parts.append(f'<text x="28" y="{y + 41}" font-size="12.5" fill="{MUTED}">{q1}</text>')
    parts.append(f'<text x="28" y="{y + 58}" font-size="12.5" fill="{MUTED}">{q2}</text>')
    parts.append(f'<text x="{W_STACK - 26}" y="{y + 58}" font-size="12" fill="{MUTED}" '
                 f'text-anchor="end">{state}</text>')
    parts.append(dot(W_STACK - 16, y + 54, fill, MUTED))
for j, (name, gloss) in enumerate(CROSS):
    x = W_STACK + GAP + j * (GAP + W_CROSS)
    parts.append(f'<rect x="{x}" y="0" width="{W_CROSS}" height="{H}" rx="6" fill="{CARD}" stroke="{RULE}"/>')
    cx, cy = x + W_CROSS / 2 + 5, H / 2
    parts.append(f'<text transform="translate({cx} {cy}) rotate(-90)" text-anchor="middle" font-size="13" '
                 f'fill="{MUTED}"><tspan font-weight="700" fill="{FG}">{name}</tspan> · {gloss}</text>')
parts.append("</svg>\n")
open("figures/layers.svg", "w").write("".join(parts))
