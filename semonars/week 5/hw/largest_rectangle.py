class Rectangle:
    heigth: int
    width: int

    def __init__(self, heigth: int, width: int = 1):
        self.heigth = heigth
        self.width = width


class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = [Rectangle(heights[0])]
        max_area = 0

        for i in heights[1:]:
            if i == stack[-1].heigth:
                stack[-1].width += 1

            elif i > stack[-1].heigth:
                stack.append(Rectangle(i))

            else:  # i < stack[-1].height
                top = Rectangle(0, 0)
                while stack and stack[-1].heigth > i:
                    stack[-1].width += top.width
                    top = stack.pop()
                    max_area = max(max_area, top.width * top.heigth)
                stack.append(Rectangle(i, 1 + (top.width if top.width else 0)))
                max_area = max(max_area, stack[-1].width * stack[-1].heigth)

        while stack:
            top = stack.pop()

            max_area = max(
                max_area,
                top.heigth * top.width
            )
            if stack:
                stack[-1].width += top.width

        return max_area


print(Solution().largestRectangleArea([2, 1, 5, 6, 2, 3]))  # 10
