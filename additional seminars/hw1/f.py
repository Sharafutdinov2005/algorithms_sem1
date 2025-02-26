n, x, y = map(int, input().split())

s, f = min(x, y), (n - 1) * max(x, y)

while s + 1 < f:
    m = (s + f) // 2
    if m // x + m // y + 1 < n:
        f = m
    else:
        s = m

print(s + min(x, y))
