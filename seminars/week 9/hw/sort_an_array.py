from typing import List
from random import randint


def sort(
    nums: List[int],
) -> List[int]:
    """
    Sorts a list of integers in ascending order.

    Time complexity: `O(n log (n))`
    """

    quick_sort(nums, 0, len(nums) - 1)

    return nums


def partition(
    array: List[int],
    begin: int,
    end: int
) -> int:
    pivot = randint(begin, end)
    array[pivot], array[end] = array[end], array[pivot]

    i = begin

    for j in range(begin, end):
        if array[j] <= array[end]:
            array[i], array[j] = array[j], array[i]
            i += 1

    array[i], array[end] = array[end], array[i]
    return i


def quick_sort(
    array: List[int],
    begin: int,
    end: int
) -> None:
    if begin >= end:
        return
    pivot = partition(array, begin, end)
    quick_sort(array, begin, pivot - 1)
    quick_sort(array, pivot + 1, end)


print(
    sort([3, 2, 1])
)
