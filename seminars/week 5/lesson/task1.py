from collections import deque


# possible symbols (), {}
def is_valid(s):
    stack = deque()
    for c in s:
        if (c == ')') and (not stack or stack.pop() != '('):
            return False
        elif (c == '}') and (not stack or stack.pop() != '{'):
            return False
        stack.append(c)

    return True


s = input()
print(is_valid(s))
