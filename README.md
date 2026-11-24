# Name: hachaichi mohamed raid
Group: DD2
Academic year: 2026/2027
Module: Algorithms and Data Structures
Language and libraries
Python 3 (version: ...).
time: time.perf_counter() and time.process_time()
memory: tracemalloc (peak memory during the sort)
Time and memory are measured in two different runs, because tracemalloc makes the program slower.
How to run
python src/main.py
python tests/test_sorting.py
The menu has the 5 algorithms, option 6 to compare them (the results are saved in results/ as csv files) and option 7 for the big array of 100000 integers (seed 42).
Algorithms
Algorithm	Best	Average	Worst	Space
Bubble Sort	O(n)	O(n^2)	O(n^2)	O(1)
Selection Sort	O(n^2)	O(n^2)	O(n^2)	O(1)
Insertion Sort	O(n)	O(n^2)	O(n^2)	O(1)
Merge Sort	O(n log n)	O(n log n)	O(n log n)	O(n)
Quick Sort	O(n log n)	O(n log n)	O(n^2)	O(log n)
Bubble Sort: compares neighbors and swaps them, stops if there was no swap in a pass.
Selection Sort: finds the minimum of the unsorted part and puts it at its place.
Insertion Sort: inserts each element in the sorted left part.
Merge Sort: splits the array in two, sorts each half and merges them.
Quick Sort: the pivot is chosen randomly, then the elements are partitioned around it. The recursion is done on the smaller part to avoid a recursion error.
Results
Machine: CPU ..., RAM ..., OS ...
(put the tables of the csv files here)
Analysis
(write your observations here: which algorithm is the best, does it match the theory, the problems you had)
