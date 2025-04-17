def merge(array: list[int], start: int, mid: int, end: int) -> int:
    left = array[start:mid + 1]
    right = array[mid + 1:end + 1]
    i = j = 0
    k = start
    inversions = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
            inversions += (mid + 1) - (start + i)
        k += 1

    while i < len(left):
        array[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        array[k] = right[j]
        j += 1
        k += 1

    return inversions


def sort(array: list[int], start: int, end: int) -> int:
    if start >= end:
        return 0

    mid = (start + end) // 2
    inv = sort(array, start, mid)
    inv += sort(array, mid + 1, end)
    inv += merge(array, start, mid, end)
    return inv


arr = [3, 1, 2]
print(sort(arr, 0, len(arr) - 1))
