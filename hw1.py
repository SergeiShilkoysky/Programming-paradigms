
## Задание:
# 1. Написать в императивном стиле процедуру для # сортировки числа в списке
# в порядке убывания (можно использовать любой алгоритм сортировки).
# 2. Написать точно такую же процедуру, но в декларативном стиле


from random import randint
from timeit import repeat

ARRAY_LENGTH = 100


def run_sorting_algorithm(algorithm, array):
    """"Determining the running time of algorithm:"""

    setup_code = f"from __main__ import {algorithm}" \
        if algorithm != "sorted" else ""

    stmt = f"{algorithm}({array})"
    times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=10)
    print(f"Algorithm: {algorithm}. Minimum execution time: {min(times)}")


def quicksort_imperative(array):
    if len(array) < 2:
        return array

    low, same, high = [], [], []
    pivot = array[randint(0, len(array) - 1)]
    for item in array:
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)
    return quicksort_imperative(low) + same + quicksort_imperative(high)


def timeSort_declarative(array):
    return sorted(array)


def timeSort2_declarative(array):
    array.sort()
    return array


if __name__ == "__main__":
    # Generate an array of `ARRAY_LENGTH` items consisting of random integer values
    array = [randint(0, 1000) for i in range(ARRAY_LENGTH)]

    # print(quicksort_imperative(array))
    # print(timeSort_declarative(array))
    # print(timeSort2_declarative(array))

    run_sorting_algorithm(algorithm="quicksort_imperative", array=array)
    run_sorting_algorithm(algorithm="timeSort_declarative", array=array)
    run_sorting_algorithm(algorithm="timeSort2_declarative", array=array)
