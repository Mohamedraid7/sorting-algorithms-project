import random


def generate(n, kind="random", seed=42):
    random.seed(seed)
    if kind == "random":
        return [random.randint(0, 100000) for _ in range(n)]
    if kind == "sorted":
        return list(range(n))
    if kind == "reverse":
        return list(range(n, 0, -1))
    if kind == "duplicates":
        return [random.randint(0, 50) for _ in range(n)]


def is_sorted(t):
    for i in range(len(t) - 1):
        if t[i] > t[i + 1]:
            return False
    return True
