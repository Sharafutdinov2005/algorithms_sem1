def approx_bin_search(arr: list, target: int) -> int:
    s, e = 0, len(arr) - 1
    while e - s > 1:
        m = (s + e) // 2
        if arr[m] == x:
            return arr[m]
        elif arr[m] > x:
            e = m
        else:
            s = m
    if abs(arr[e] - x) < abs(arr[s] - x):
        return arr[e]
    else:
        return arr[s]


n, k = map(int, input().split())
arr = list(map(int, input().split()))
ask = list(map(int, input().split()))

for x in ask:
    print(approx_bin_search(arr, x))
