from sorting import ALGOS
from utils import generate
from benchmark import measure, compare, QUADRATIC

names = list(ALGOS)


def read_int(msg):
    try:
        return int(input(msg))
    except ValueError:
        print("invalid input")
        return None


def choose_type():
    print("1. random  2. sorted  3. reverse  4. duplicates")
    c = input("type: ")
    types = {"1": "random", "2": "sorted", "3": "reverse", "4": "duplicates"}
    if c not in types:
        print("invalid choice")
        return None
    return types[c]


def run_one(name):
    n = read_int("array size: ")
    if n is None or n <= 0:
        print("invalid size")
        return
    kind = choose_type()
    if kind is None:
        return
    if name in QUADRATIC and n > 20000:
        if input("this can be very slow, continue? (y/n) ") != "y":
            return
    data = generate(n, kind)
    if n <= 20:
        print("before:", data)
        t = data.copy()
        ALGOS[name](t)
        print("after: ", t)
    w, c, m, ok = measure(ALGOS[name], data)
    print(name, "- n =", n, "-", kind)
    print("wall time : %.2f ms" % w)
    print("cpu time  : %.2f ms" % c)
    print("memory    : %.3f MB" % m)
    print("sorted    :", ok)


def big_array():
    print("array of 100000 random integers (seed 42)")
    big = generate(100000, "random", 42)
    small = generate(10000, "random", 42)
    for name in names:
        data = small if name in QUADRATIC else big
        w, c, m, ok = measure(ALGOS[name], data, 1)
        print("%-16s n=%6d  %10.2f ms  %8.3f MB  %s" % (name, len(data), w, m, ok))
    print("bubble, selection and insertion were tested on 10000 elements (too slow)")


def main():
    while True:
        print("\n=========== SORTING ALGORITHMS ===========")
        print("1. Bubble Sort")
        print("2. Selection Sort")
        print("3. Insertion Sort")
        print("4. Merge Sort")
        print("5. Quick Sort")
        print("6. Compare all algorithms")
        print("7. Big array example")
        print("0. Exit")
        choice = input("Your choice: ")
        if choice == "0":
            break
        elif choice in ["1", "2", "3", "4", "5"]:
            run_one(names[int(choice) - 1])
        elif choice == "6":
            kind = choose_type()
            if kind:
                compare(kind, "results/comparison_" + kind + ".csv")
        elif choice == "7":
            big_array()
        else:
            print("invalid choice")


main()
