def heapify(
    array: list[int]
) -> None:
    for i in range(len(array)//2 + 1, -1, -1):
        sift_down(array, i)


def sift_down(
    heap: list[int],
    length: int,
    i: int = 0
):
    while True:
        child1 = 2 * i + 1
        child2 = 2 * i + 2

        # no child
        if child1 >= length:
            break

        # single child

        # if child is greater than parent
        if child2 >= length:
            if heap[child1] < heap[i]:
                heap[child1], heap[i] = heap[i], heap[child1]
            break

        # two children

        # if child1 is greater than parent
        if heap[child1] < heap[child2] and heap[child1] < heap[i]:
            heap[child1], heap[i] = heap[i], heap[child1]
            i = child1

        # if child2 is greater than parent
        elif heap[child2] < heap[i]:
            heap[child2], heap[i] = heap[i], heap[child2]
            i = child2

        # no child is greater than parent
        else:
            break


def heap_sort(
    array: list[int]
) -> None:
    heapify(array)

    for i in range(len(array)):
        array[-i - 1], array[0] = array[0], array[-i - 1]
        sift_down(array, len(array) - i - 1, 0)


a = [1, 2, 100, 3, 4, 5]
heap_sort(a)
print(a)
