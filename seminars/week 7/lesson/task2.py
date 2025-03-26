# p = (i - 1) // 2
# l = 2i + 1
# r = 2i + 2


class Element:
    value: int
    index: int

    def __init__(self, value: int, index: int):
        self.value, self.index = value, index


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


def push_heap(heap: list[int], value: int) -> None:
    """Pushes a value into the heap."""
    heap.append(value)
    sift_up(heap, len(heap) - 1)


def pop_heap(heap: list[int]) -> int:
    """Pops a value from the heap."""
    if len(heap) == 0:
        return None
    if len(heap) == 1:
        return heap.pop()


def heapify(elements: list):
    heap = []
    for i in range(len(elements)//2 + 1, -1, -1):
        sift_down(heap, i)
    return heap


def count_of_eatings(heap, k):
    count = 0
    while len(heap) > 0:
        mass_sum = 0
        elements = []
        while len(heap) > 0 and mass_sum + heap[0] <= k:
            elements.append(pop_heap(heap, 0))
            mass_sum += elements[-1]
        for element in elements:
            if element > 1:
                push_heap(heap, element / 2)
        count += 1
    return count


n = int(input())
a = list(map(int, input().split()))
k = int(input())
heap = heapify(a)
print(count_of_eatings(heap, k))
