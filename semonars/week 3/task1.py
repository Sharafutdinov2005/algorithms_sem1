from typing import Optional


def binary_search_rec(
    a: list[int],
    x: int,
    s: int,
    f: int
) -> Optional[int]:
    m = (s + f) // 2
    if m == s:
        return None
    if a[m] == x:
        return m
    if a[m] > x:
        return binary_search_rec(a, x, s, m)
    return binary_search_rec(a, x, m, f)
