from typing import List
# from random import randint


def partition(
    array: List[int],
    begin: int,
    end: int
) -> int:
    """
    Partition the array around a pivot element
    such that all elements less than the pivot are on the left of it,
    all elements greater than the pivot are on the right of it,
    and all elements equal to the pivot are on the left of it.
    """

    # pivot = randint(0, len(array) - 1)

    # array[pivot], array[-1] = array[-1], array[pivot]

    # i, j = 0, len(array) - 2

    # while i <= j:
    #     if array[i] <= array[-1]:
    #         i += 1
    #     elif array[i] > array[-1]:
    #         while array[j] > array[-1]:
    #             j -= 1
    #         array[i], array[j] = array[j], array[i]
    #         i += 1
    #         j -= 1
    # array[i], array[-1] = array[-1], array[i]

    # print([3, 1, 2])

    # return i
    pass


def quick_sort(
    array: List[int],
    begin: int,
    end: int
) -> None:
    if begin == end:
        return
    quick_sort(array, begin, partition(array, begin, end) - 1)
    quick_sort(array, partition(array, begin, end) + 1, end)


def find_k_statistics(
    array: List[int],
    k: int
) -> int:
    begin = 0
    end = len(array) - 1
    while begin <= end:
        pivot = partition(array, begin, end)
        if pivot == k:
            return array[pivot]
        elif pivot < k:
            begin = pivot + 1
        else:
            end = pivot - 1
