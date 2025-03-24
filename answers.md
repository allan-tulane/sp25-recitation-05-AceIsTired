# CMPS 2200 Reciation 5
## Answers
**Name:** Jamari Ross

Place all written answers from `recitation-05.md` here for easier grading.







- **1b.**
[Running] python -u "c:\Users\Jamari\Documents\Coding Projects\sp25-recitation-05-AceIsTired-main\main.py"

|      n |   qsort-fixed-pivot |   qsort-random-pivot |
|--------|---------------------|----------------------|
|    100 |               0.010 |                0.065 |
|    200 |               0.015 |                0.151 |
|    500 |               0.037 |                0.401 |
|   1000 |               0.067 |                0.839 |
|   2000 |               0.154 |                2.125 |
|   5000 |               0.304 |                6.666 |
|  10000 |               0.634 |               13.182 |
|  20000 |               1.501 |               28.177 |
|  50000 |               4.634 |               54.768 |
| 100000 |               8.296 |              168.499 |

Both fixed and random qsort run at $O(n \log n)$ average time complexity, but qsort-fixed-pivot generally runs faster as the list size increased due to it not picking poor pivot selection.




- **1c.**
[Running] python -u "c:\Users\Jamari\Documents\Coding Projects\sp25-recitation-05-AceIsTired-main\main.py"

|      n |   qsort-fixed-pivot |   qsort-random-pivot |   tim-sort |     ssort |
|--------|---------------------|----------------------|------------|-----------|
|    100 |               0.091 |                0.109 |      0.006 |     0.135 |
|    200 |               0.174 |                0.215 |      0.012 |     0.540 |
|    500 |               0.533 |                0.672 |      0.033 |     2.995 |
|   1000 |               1.503 |                1.458 |      0.077 |    11.375 |
|   2000 |               2.802 |                3.302 |      0.183 |    37.971 |
|   5000 |               6.858 |                8.385 |      0.433 |   274.947 |
|  10000 |              15.124 |               18.230 |      0.963 |  1065.478 |
|  20000 |              34.326 |               35.467 |      2.048 |  4910.873 |
|  50000 |              90.198 |              108.300 |      7.859 | 34204.204 |
| 100000 |             208.464 |              213.987 |     12.978 |           |

Python's timsort function is still faster than both quicksort and selection sort implementations.