"""Print WCAG 2.x contrast ratios for the Modern theme tokens.

Usage: python docs/tools/contrast.py
Keep the values in sync with docs/DESIGN-SYSTEM.md and themes/Modern.less.
"""


def luminance(hex_color):
    h = hex_color.lstrip("#")
    channels = [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    linear = [c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
              for c in channels]
    return 0.2126 * linear[0] + 0.7152 * linear[1] + 0.0722 * linear[2]


def contrast(a, b):
    hi, lo = sorted((luminance(a), luminance(b)), reverse=True)
    return (hi + 0.05) / (lo + 0.05)


PAIRS = [
    # (label, foreground, background, minimum)
    ("text on panel", "#dfe1e5", "#282a2e", 4.5),
    ("text on sunken", "#dfe1e5", "#1f2124", 4.5),
    ("text on raised", "#dfe1e5", "#383b40", 4.5),
    ("text-secondary on panel", "#a3a8b0", "#282a2e", 4.5),
    ("text-secondary on sunken", "#a3a8b0", "#1f2124", 4.5),
    ("white on accent", "#ffffff", "#3574d4", 4.5),
    ("accent-line on panel", "#4a8fe7", "#282a2e", 3.0),
    ("warning on panel", "#e3a33b", "#282a2e", 4.5),
    ("error on panel", "#ef6b63", "#282a2e", 4.5),
    ("success on panel", "#3fb950", "#282a2e", 4.5),
    ("tooltip text", "#dfe1e5", "#111214", 4.5),
]

if __name__ == "__main__":
    failed = 0
    for label, fg, bg, minimum in PAIRS:
        ratio = contrast(fg, bg)
        ok = ratio >= minimum
        failed += not ok
        print(f"{'pass' if ok else 'FAIL'}  {ratio:5.2f}  (min {minimum})  {label}")
    raise SystemExit(1 if failed else 0)
