class Column:
    value: int
    index: int

    def __init__(self, value: int, index: int):
        self.value = value
        self.index = index

    def __repr__(self):
        return f"Column(value={self.value}, index={self.index})"


def calculate_water(map):
    ans = 0
    previous_hight = [Column(map[0], 0)]
    for i in range(1, len(map)):
        if len(previous_hight) == 1 and map[i] > previous_hight[0].value:
            previous_hight[0] = Column(map[i], i)
            continue

        if map[i] < previous_hight[-1].value:
            previous_hight.append(Column(map[i], i))

        elif map[i] > previous_hight[-1].value:
            flag = None
            while (
                len(previous_hight) > 1
                and map[i] > previous_hight[-2].value
            ):
                flag = True
                ans += (
                    (previous_hight[-2].value - previous_hight[-1].value) *
                    (i - previous_hight[-1].index)
                )
                previous_hight.pop()

            if flag:
                if len(previous_hight) == 1:
                    previous_hight[0] = Column(map[i], i)

            if len(previous_hight) > 1 and map[i] == previous_hight[-2].value:
                ans += (
                    (previous_hight[-2].value - previous_hight[-1].value) *
                    (i - previous_hight[-1].index)
                )
                previous_hight.pop()

            if (
                len(previous_hight) > 1 and
                map[i] < previous_hight[-2].value and
                map[i] > previous_hight[-1].value
            ):
                ans += (
                    (map[i] - previous_hight[-1].value) *
                    (i - previous_hight[-1].index)
                )
                previous_hight[-1].value = map[i]
    return ans


n = int(input())
a = list(map(int, input().split()))

print(calculate_water(a))
