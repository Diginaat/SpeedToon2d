"""Summarise a timeline paint log written by SPEEDTOON2D_TIMELINE_PAINT_LOG.

Usage: python test-scenes/tools/paint_stats.py <log> [<log> ...]
Each log line is "<microseconds> <width>x<height>" for one repaint.
"""
import statistics
import sys
from pathlib import Path


def summarise(path):
    if not Path(path).exists():
        print(f"{path}: not found")
        return
    times = []
    full = 0
    with open(path, encoding="ascii") as f:
        for line in f:
            parts = line.split()
            if len(parts) != 2:
                continue
            times.append(int(parts[0]) / 1000.0)
            w, h = (int(v) for v in parts[1].split("x"))
            full += w * h > 200 * 200
    if not times:
        print(f"{path}: no samples")
        return
    times.sort()
    p95 = times[min(len(times) - 1, int(len(times) * 0.95))]
    print(f"{path}: {len(times)} repaints ({full} larger than 200x200), "
          f"mean {statistics.mean(times):.2f} ms, median "
          f"{statistics.median(times):.2f} ms, p95 {p95:.2f} ms, "
          f"max {times[-1]:.2f} ms")


if __name__ == "__main__":
    for arg in sys.argv[1:]:
        summarise(arg)
