class Point:
    x: int
    y: int

    def __init__(
        self,
        x,
        y
    ) -> None:
        self.x = x
        self.y = y

    def __lt__(
        self,
        other: 'Point'
    ) -> bool:
        return self.x < other.x or (self.x == other.x and self.y < other.y)

    def __str__(
        self
    ) -> str:
        return f"{self.x} {self.y}"


n = int(input())
points = [Point(*map(int, input().split())) for _ in range(n)]
points.sort()
print("result:", *points, sep='\n')
