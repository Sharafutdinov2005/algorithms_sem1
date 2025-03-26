def check_jumps(
    jump_length: int,
    jumps_amount: int,
    points: str
) -> bool:
    """
    This function checks if it's possible to jump over all points in a list
    with a given amount of jumps and a given length of the jump.
    """
    position = 0
    for _ in range(jumps_amount):
        new_position = position
        for point in range(jump_length):
            if position + point >= len(points) - 1:
                return True
            if points[position + point] == '1':
                new_position = position + point
        if new_position == position:
            return False
        position = new_position


def optimize(
    maximum_jumps: int,
    points: str,
) -> int:
    """
    This function finds the minimum value of maximum jump's length.
    """
    left, right = 0, len(points)

    while left < right + 1:
        middle = (left + right) // 2
        if check_jumps(middle, maximum_jumps, points):
            right = middle - 1
        else:
            left = middle + 1

    return left


n, k = map(int, input().split())
s = input() + '1'
print(optimize(k, s))
