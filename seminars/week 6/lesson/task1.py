# p = (i - 1) // 2
# l = 2i + 1
# r = 2i + 2


def sift_up(heap: list[int], i: int) -> None:
    """Sifts up the heap from the given index i."""
    while i > 0:
        parent = (i - 1) // 2
        if heap[parent] <= heap[i]:
            break
        heap[parent], heap[i] = heap[i], heap[parent]
        i = parent


def sift_down(heap: list[int], i: int) -> None:
    """Sifts down the heap from the given index i."""
    while True:
        child1 = 2 * i + 1
        child2 = 2 * i + 2

        # no child
        if child1 >= len(heap):
            break

        # single child

        # if child is greater than parent
        if child2 >= len(heap):
            if heap[child1] > heap[i]:
                heap[child1], heap[i] = heap[i], heap[child1]
            break

        # two children

        # if child1 is greater than parent
        if heap[child1] > heap[child2] and heap[child1] > heap[i]:
            heap[child1], heap[i] = heap[i], heap[child1]
            i = child1

        # if child2 is greater than parent
        elif heap[child2] > heap[i]:
            heap[child2], heap[i] = heap[i], heap[child2]
            i = child2

        # no child is greater than parent
        else:
            break
