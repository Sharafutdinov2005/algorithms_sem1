class Rectangle:
    height: int
    width: int

    def __init__(self, w, h):
        self.height = h
        self.width = w


def find_max_square(histogramm: list[Rectangle]):
    stack = [histogramm[0]]
    max_square = 0

    for i in histogramm[1:]:
        if i.height == stack[-1].height:
            stack[-1].width += i.width

        elif i.height > stack[-1].height:
            stack.append(i)

        else:
            while stack and stack[-1].height > i.height:
                top = stack.pop()

                max_square = max(
                    max_square,
                    top.height * top.width
                )

                stack[-1].width += top.width

            i.width += top.width
            max_square = max(
                    max_square,
                    i.height * i.width
                )

            stack.append(i)

        while stack:
            top = stack.pop()

            max_square = max(
                max_square,
                top.height * top.width
            )
            if stack:
                stack[-1].width += top.width

        return max_square


n = int(input())
histogramm = []

for i in range(n):
    w, h = map(int, input().split())
    histogramm.append(
        Rectangle(
            w, h
        )
    )

print(find_max_square(histogramm))
