class Segment:
    start: int
    end: int

    def __init__(
        self,
        start: int,
        end: int
    ) -> None:
        self.start = start
        self.end = end

    def __lt__(
        self,
        other: 'Segment'
    ) -> bool:
        return self.start < other.start


def count_colored(
    array: list[Segment]
) -> int:
    colored = 0
    start = array[0].start
    end = array[0].end

    for i in range(1, len(array)):
        if array[i].start < end:
            end = max(array[i].end, end)
        else:
            colored += end - start
            start = array[i].start
            end = array[i].end

    return colored + end - start


n = int(input())
a = [Segment(*map(int, input().split())) for _ in range(n)]
a.sort()
print(count_colored(a))
