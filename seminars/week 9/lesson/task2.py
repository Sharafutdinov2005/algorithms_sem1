class box:
    def __init__(self, a, b, number):
        self.width = min(a, b)
        self.height = max(a, b)
        self.number = number

    def __lt__(
        self,
        other
    ) -> bool:
        return self.width < other.width and self.height < other.height

    def __gt__(
        self,
        other
    ) -> bool:
        return self.width > other.width and self.height > other.height

    def __str__(
        self
    ) -> str:
        return str(self.number)


n = int(input())
boxes = []

for i in range(n):
    a, b = map(int, input().split())
    boxes.append(box(a, b, i + 1))

boxes.sort()

print(*boxes)
