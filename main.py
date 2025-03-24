import random, time
import tabulate
import sys


sys.setrecursionlimit(100000)

def ssort(L):
    ### selection sort
    if (len(L) <= 1):
        return(L)
    else:
        m = L.index(min(L))
        # print('selecting minimum %s' % L[m])
        L[0], L[m] = L[m], L[0]
        # print('recursively sorting L=%s\n' % L[1:])
        return [L[0]] + ssort(L[1:])

def qsort(a, pivot_fn):
    if len(a) <= 1: #base case
        return a

    pivot = pivot_fn(a) #pick the pivot using the provided func

    left = [x for x in a if x < pivot]
    middle = [x for x in a if x == pivot]
    right = [x for x in a if x > pivot]

    return qsort(left, pivot_fn) + middle + qsort(right, pivot_fn)


def time_search(sort_fn, mylist):
    start = time.time()
    sort_fn(mylist)
    return (time.time() - start) * 1000
    ###

def compare_sort(sizes=[100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000]):
    """
    Compare the running time of different sorting algorithms.

    Returns:
      A list of tuples of the form
      (n, linear_search_time, binary_search_time)
      indicating the number of milliseconds it takes
      for each method to run on each value of n
    """
    ### TODO - sorting algorithms for comparison
    

    result = []
    for size in sizes:
        # create list in ascending order
        mylist = list(range(size))
        # shuffles list if needed
        random.shuffle(mylist)

        qsort_fixed_pivot = time_search(lambda a: qsort(a, lambda b: b[0]), mylist)
        qsort_random_pivot = time_search(lambda a: qsort(a, lambda b: random.choice(b)), mylist)
        tim_sort = time_search(lambda a: sorted(a), mylist)
        s_sort = time_search(ssort, mylist) if int(size) <= 50000 else None

        result.append([
            len(mylist),
            qsort_fixed_pivot,
            qsort_random_pivot,
            tim_sort,
            s_sort
            
        ])

        
    return result
    ###

def print_results(results):
    """ change as needed for comparisons """
    print(tabulate.tabulate(results,
                            headers=['n', 'qsort-fixed-pivot', 'qsort-random-pivot', 'tim-sort', 'ssort'],
                            floatfmt=".3f",
                            tablefmt="github"))

def test_print():
    print_results(compare_sort())

random.seed()
test_print()
