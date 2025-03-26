from typing import Any, Optional


class DoubleLinkedKnot():
    value: Any
    prev: Optional['DoubleLinkedKnot']
    next: Optional['DoubleLinkedKnot']

    def __init__(
        self,
        value: Any
    ) -> None:
        """
        Creates `DoubleLinkedKnot` object.
        """
        self.value = value
        self.prev = None
        self.next = None

    def __add__(
        self,
        next: Optional['DoubleLinkedKnot']
    ):
        self.next = next
        if next:
            next.prev = self


def delete_negative(
    dl_start: DoubleLinkedKnot
) -> DoubleLinkedKnot:
    while dl_start and dl_start.value < 0:
        dl_start = dl_start.next

    dl_end = dl_start

    while dl_end:
        if dl_end.value < 0:
            prev = dl_end.prev
            next = dl_end.next
            if prev:
                prev.next = next
            if next:
                next.prev = prev
        dl_end = dl_end.next

    return dl_start


a = list(map(int, input().split()))

dl_start = DoubleLinkedKnot(a[0])
dl_end = dl_start

for i in range(1, len(a)):
    dl_end + DoubleLinkedKnot(a[i])
    dl_end = dl_end.next

dl_start = delete_negative(dl_start)

while dl_start:
    print(dl_start.value, end=' ')
    dl_start = dl_start.next
