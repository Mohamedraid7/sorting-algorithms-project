import csv
import os
import time
import tracemalloc

from sorting import ALGOS
from utils import generate, is_sorted

QUADRATIC = ["Bubble Sort", "Selection Sort", "Insertion Sort"]
SIZES = [1000, 5000, 10000, 50000, 100000]
LIMIT = 10000


def measure(func, data, runs=3):
    total_wall = 0
    total_cpu = 0
    ok = True
    for _ in range(runs):
        t = data.copy()
        w1 = time.perf_counter()
        c1 = time.process_time()
        func(t)
        c2 = time.process_time()
        w2 = time.perf_counter()
        total_wall += (w2 - w1) * 1000
        total_cpu += (c2 - c1) * 1000
        if not is_sorted(t):
            ok = False

    t = data.copy()
    tracemalloc.start()
    func(t)
    peak = tracemalloc.get_traced_memory()[1]
    tracemalloc.stop()

    return total_wall / runs, total_cpu / runs, peak / (1024 * 1024), ok


def compare(kind, filename):
    rows = []
    for n in SIZES:
        data = generate(n, kind)
        results = []
        for name, func in ALGOS.items():
            if name in QUADRATIC and n > LIMIT:
                results.append([name, n, kind, None, None, None])
            else:
                w, c, m, ok = measure(func, data)
                results.append([name, n, kind, round(w, 2), round(c, 2), round(m, 3)])
        done = sorted([r for r in results if r[3] is not None], key=lambda r: r[3])
        for r in results:
            if r[3] is None:
                r.append("-")
            else:
                r.append(done.index(r) + 1)
        rows += results

    print("\n%-16s %8s %12s %10s %10s %6s" % ("Algorithm", "Size", "Time (ms)", "CPU (ms)", "Mem (MB)", "Rank"))
    for r in rows:
        if r[3] is None:
            print("%-16s %8d %12s %10s %10s %6s" % (r[0], r[1], "skipped", "-", "-", "-"))
        else:
            print("%-16s %8d %12.2f %10.2f %10.3f %6d" % (r[0], r[1], r[3], r[4], r[5], r[6]))

    os.makedirs("results", exist_ok=True)
    with open(filename, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["algorithm", "size", "type", "time_ms", "cpu_ms", "memory_mb", "rank"])
        w.writerows(rows)
    print("saved in", filename)
