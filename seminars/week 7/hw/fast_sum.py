def heapify_min(
    array: list[list]
) -> None:
    for i in range(len(array)//2 + 1, -1, -1):
        sift_down(array, i)


def sift_up(heap: list[int], i: int) -> None:
    """Sifts up the heap from the given index i."""
    while i > 0:
        parent = (i - 1) // 2
        if heap[parent] <= heap[i]:
            break
        heap[parent], heap[i] = heap[i], heap[parent]
        i = parent


def insert(
    heap: list[int],
    elem: int
) -> None:
    """Inserts a value into the heap."""
    heap.append(elem)
    sift_up(heap, len(heap) - 1)


def sift_down(
    heap: list[int],
    i: int
) -> None:
    while True:
        child1 = 2 * i + 1
        child2 = 2 * i + 2

        # no child
        if child1 >= len(heap):
            break

        # single child

        # if child is less than parent
        if child2 >= len(heap):
            if heap[child1] < heap[i]:
                heap[child1], heap[i] = heap[i], heap[child1]
            break

        # two children

        # if child1 is greater than parent
        if (heap[child1] < heap[child2] and
                heap[child1] < heap[i]):
            heap[child1], heap[i] = heap[i], heap[child1]
            i = child1

        # if child2 is greater than parent
        elif heap[child2] < heap[i]:
            heap[child2], heap[i] = heap[i], heap[child2]
            i = child2

        # no child is greater than parent
        else:
            break


def delete_min(
    heap: list[int]
) -> int:
    minimum = heap[0]
    heap[0] = heap.pop()
    sift_down(heap, 0)
    return minimum


def sum_time_counter(
    numbers: list[int]
) -> int:
    if len(numbers) <= 1:
        return 0

    heapify_min(numbers)
    sum_time_counter = 0

    while len(numbers) > 2:
        minimum = delete_min(numbers)
        second_minimum = delete_min(numbers)

        sum_time_counter += minimum + second_minimum

        insert(numbers, minimum + second_minimum)

    sum_time_counter += (numbers[0] + numbers[1])

    return sum_time_counter


n = int(input())
numbers = list(map(int, input().split()))
print(sum_time_counter(numbers))
