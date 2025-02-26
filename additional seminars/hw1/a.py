def find_number(arr: list, x: int) -> bool:
    s, e = 0, len(arr) - 1
    while s <= e:
        mid = (s + e) // 2
        if arr[mid] == x:
            return True
        elif arr[mid] < x:
            s = mid + 1
        else:
            e = mid - 1


n, q = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
ask = list(map(int, input().split()))

for x in ask:
    if find_number(arr, x):
        print("YES")
    else:
        print("NO")
