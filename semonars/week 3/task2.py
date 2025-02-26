def is_growing(x_prev, x, x_next):
    return x_prev < x < x_next


def is_max(x_prev, x, x_next):
    return x_prev < x > x_next


def find_final(a):
    i = 1
    while i < len(a) and is_growing(a[i - 1], a[1], a[i + 1]):
        i *= 2
    return min(i, len(a) - 2)


def find_max(a):
    f = find_final(a)
    s = f // 2
    while s < f:
        m = (s + f) // 2
        if is_max(a[m - 1], a[m], a[m + 1]):
            return m
        if is_growing(a[m - 1], a[m], a[m + 1]):
            s = m
        else:
            f = m
