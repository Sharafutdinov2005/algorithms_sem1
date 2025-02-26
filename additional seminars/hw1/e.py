def solve(a: int, b: int, c: int, d: int) -> float:
    sign_a = (a / abs(a))
    a *= sign_a
    b *= sign_a
    c *= sign_a
    d *= sign_a

    left, right = -5e3, 5e3
    while left < right:
        m = (left + right) / 2
        t = a * m ** 3 + b * m ** 2 + c * m + d
        if abs(t) < 1e-12:
            return m
        elif t > 1e-12:
            right = m
        else:
            left = m


a, b, c, d = map(int, input().split())
print(solve(a, b, c, d))
