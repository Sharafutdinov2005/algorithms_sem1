def check_cut(
    short_left,
    long_left,
    short_right,
    long_right
):
    return short_left <= long_right and long_left <= short_right


def find_median(short, long):
    elements_amount = len(short) + len(long)
    half_elements_amount = elements_amount // 2

    if len(long) < len(short):
        short, long = long, short

    if not short:
        return (
            long[half_elements_amount]
            if elements_amount % 2 else
            (long[half_elements_amount - 1] + long[half_elements_amount]) / 2.0
        )

    left, right = 0, len(short) - 1
    while True:
        mid_short = (left + right) // 2
        mid_long = half_elements_amount - mid_short - 2

        short_left = (
            short[mid_short]
            if mid_short >= 0 else
            float('-inf')
        )
        short_right = (
            short[mid_short + 1]
            if (mid_short + 1) < len(short) else
            float('inf')
        )

        long_left = (
            long[mid_long]
            if mid_long >= 0 else
            float('-inf')
        )
        long_right = (
            long[mid_long + 1]
            if (mid_long + 1) < len(long) else
            float('inf')
        )

        if check_cut(short_left, long_left, short_right, long_right):
            if elements_amount % 2:
                return min(short_right, long_right)
            else:
                return (
                    max(short_left, long_left) + min(short_right, long_right)
                ) / 2
        elif short_left > long_right:
            right = mid_short - 1
        else:  # short_right < long_left
            left = mid_short + 1


a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(find_median(a, b))
