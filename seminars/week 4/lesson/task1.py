def delete_negative_numbers(a):
    i, j = 0, len(a) - 1
    while i < j:
        if a[i] < 0:
            a[i], a[j] = a[j], a[i]
            j -= 1
        while a[j] < 0 and i < j:
            j -= 1
        i += 1

    return a[:i]


a = list(map(int, input().split()))
print(delete_negative_numbers(a))
