import random


def bubble_sort(t):
    n = len(t)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if t[j] > t[j + 1]:
                t[j], t[j + 1] = t[j + 1], t[j]
                swapped = True
        if not swapped:
            break


def selection_sort(t):
    n = len(t)
    for i in range(n - 1):
        m = i
        for j in range(i + 1, n):
            if t[j] < t[m]:
                m = j
        t[i], t[m] = t[m], t[i]


def insertion_sort(t):
    for i in range(1, len(t)):
        x = t[i]
        j = i - 1
        while j >= 0 and t[j] > x:
            t[j + 1] = t[j]
            j -= 1
        t[j + 1] = x


def merge_sort(t):
    if len(t) <= 1:
        return
    mid = len(t) // 2
    left = t[:mid]
    right = t[mid:]
    merge_sort(left)
    merge_sort(right)
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            t[k] = left[i]
            i += 1
        else:
            t[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        t[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        t[k] = right[j]
        j += 1
        k += 1


def partition(t, low, high):
    r = random.randint(low, high)
    t[r], t[high] = t[high], t[r]
    pivot = t[high]
    i = low - 1
    for j in range(low, high):
        if t[j] <= pivot:
            i += 1
            t[i], t[j] = t[j], t[i]
    t[i + 1], t[high] = t[high], t[i + 1]
    return i + 1


def quick(t, low, high):
    while low < high:
        p = partition(t, low, high)
        if p - low < high - p:
            quick(t, low, p - 1)
            low = p + 1
        else:
            quick(t, p + 1, high)
            high = p - 1


def quick_sort(t):
    quick(t, 0, len(t) - 1)


ALGOS = {
    "Bubble Sort": bubble_sort,
    "Selection Sort": selection_sort,
    "Insertion Sort": insertion_sort,
    "Merge Sort": merge_sort,
    "Quick Sort": quick_sort,
}
