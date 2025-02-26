def find_right_board(arr: list, x: int) -> int:
    s, e = 0, len(arr) - 1
    while e > s + 1:
        m = (s + e) // 2
        if arr[m] > x:
            e = m
        else:
            s = m
    if arr[e] == x:
        return e
    if arr[s] == x:
        return s


def find_left_board(arr: list, x: int) -> int:
    s, e = 0, len(arr) - 1
    while e > s + 1:
        m = (s + e) // 2
        if arr[m] < x:
            s = m
        else:
            e = m
    if arr[s] == x:
        return s
    if arr[e] == x:
        return e


def find_amount(arr: list, x: int) -> int:
    l, r = find_left_board(arr, x), find_right_board(arr, x)
    if r is None:
        return 0
    if l == r:
        return 1
    return r - l + 1


n = int(input())
arr = list(map(int, input().split()))
arr.sort()
m = int(input())
ask = list(map(int, input().split()))

for x in ask:
    print(find_amount(arr, x))
