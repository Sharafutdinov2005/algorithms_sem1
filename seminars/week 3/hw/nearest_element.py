def find_nearest(
    element,
    elements
):
    if len(elements) == 1:
        return 0 if elements[0] >= element else len(elements)

    left, right = 0, 1

    while right <= len(elements) - 1:
        if element <= elements[right]:
            break
        right *= 2

    while left < right - 1:
        middle = (left + right) // 2
        if element == elements[middle]:
            return middle
        elif elements[middle] < element:
            left = middle
        else:
            right = middle

    return left if element <= elements[left] else right


def find_nearest_element(
    source,
    elements
):
    if not elements or not source:
        return len(elements)
    for element in source:
        yield find_nearest(element, elements)


elements = list(map(int, input().split()))
source = list(map(int, input().split()))
for element in find_nearest_element(source, elements):
    if element is not None:
        print(element, end=' ')
