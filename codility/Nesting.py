S = "(()(())()"


def solution(S):

    mapping = { "(":")"}
    stack = []

    for x in S:
        if x in ["(",")"]:
            if mapping.has_key(x): stack.append(x)
            elif len(stack) >0 and mapping[stack[-1]] == x : stack.pop()
            else: return 0

    if len(stack) == 0:
        return 1
    else:
        return 0


print(solution(S))