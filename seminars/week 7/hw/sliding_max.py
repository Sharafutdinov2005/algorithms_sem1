# p = (i - 1) // 2
# l = 2i + 1
# r = 2i + 2


class Element:
    value: int
    index: int

    def __init__(self, value: int, index: int):
        self.value, self.index = value, index


def sift_up(heap: list[Element], i: int) -> None:
    """Sifts up the heap from the given index i."""
    while i > 0:
        parent = (i - 1) // 2
        if heap[parent].value >= heap[i].value:
            break
        heap[parent], heap[i] = heap[i], heap[parent]
        i = parent


def sift_down(heap: list[Element], i: int) -> None:
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
            if heap[child1].value > heap[i].value:
                heap[child1], heap[i] = heap[i], heap[child1]
            break

        # two children

        # if child1 is greater than parent
        if (heap[child1].value < heap[child2].value and
                heap[child1].value < heap[i].value):
            heap[child1], heap[i] = heap[i], heap[child1]
            i = child1

        # if child2 is greater than parent
        elif heap[child2].value < heap[i].value:
            heap[child2], heap[i] = heap[i], heap[child2]
            i = child2

        # no child is greater than parent
        else:
            break


def insert(heap: list[Element], elem: Element) -> None:
    """Inserts a value into the heap."""
    heap.append(elem)
    sift_up(heap, len(heap) - 1)


def delete_max(heap: list[Element]) -> Element:
    maximum = heap[0]
    heap[0] = heap.pop()
    sift_down(heap, 0)
    return maximum


n, k = map(int, input().split())
a = list(map(int, input().split()))
heap = []

for i in range(n):
    insert(heap, Element(value=a[i], index=i))
    if i + 1 >= k:
        while heap[0].index < i + 1 - k:
            delete_max(heap)
        print(heap[0].value, end=" ")
