def merge(
    array: list[int],
    start: int,
    mid: int,
    end: int
) -> None:
    if start == end - 1:
        a = array[start]
        b = array[end]
        array[start] = min(a, b)
        array[end] = max(a, b)
        return

    pointer1 = 0
    pointer2 = 0

    result = []

    while start + pointer1 <= mid and mid + 1 + pointer2 <= end:
        if array[start + pointer1] <= array[mid + 1 + pointer2]:
            result.append(array[start + pointer1])
            pointer1 += 1

        else:
            result.append(array[mid + 1 + pointer2])
            pointer2 += 1

    while start + pointer1 <= mid:
        result.append(array[start + pointer1])
        pointer1 += 1

    while mid + 1 + pointer2 <= end:
        result.append(array[mid + 1 + pointer2])
        pointer2 += 1

    for i in range(len(result)):
        array[start + i] = result[i]


def sort(
    array: list[int]
) -> None:
    cut = 2
    while len(array) >= cut:
        for i in range(0, len(array) + 1, cut):
            start = i
            end = min(i + cut - 1, len(array) - 1)
            mid = (start + end) // 2
            merge(array, start, mid, end)
        cut *= 2


a = [2, 1, 3, -1, 0, 7, 5, 6]
sort(a)
print(a)
