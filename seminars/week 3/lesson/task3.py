def get_closest(element, a, b):
    return (
        a if abs(element - a) < abs(element - b) else b
    )


def find_final(a, x):
    i = 1
    while a[i] < x:
        i *= 2
    return i


def bin_search(a, x):
    f = find_final(a, x)
    s = f // 2
    while f > s + 1:
        m = (s + f) // 2
        if a[m] == x:
            return m
        if a[m] > x:
            f = m
        else:
            s = m

    ans = get_closest(x, a[s], a[f])

    if a[s] == ans:
        return s
    else:
        return f


def find_nearest(a, b):
    ans = []
    for x in b:
        ans.append(bin_search(a, x))
    return ans
