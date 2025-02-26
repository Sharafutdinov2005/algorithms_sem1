def solve(c: float) -> float:
    left, right = 0, c
    while left < right:
        m = (left + right) / 2
        if abs(m ** 4 + m - c) < 1e-6:
            return m ** 2
        elif m ** 4 + m < c:
            left = m
        else:
            right = m


c = float(input())
print(solve(c))
