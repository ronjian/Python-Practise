H = [8, 8, 5, 7 ,9, 8, 7, 4, 8]

def solution(H):

    stack = []
    block = 0

    for x in H:
        #pop out bigger wall before
        while len(stack) > 0:
            if x < stack[-1]:
                stack.pop()
            else:
                break

        #if the wall appear before, than not need to accumulate
        if len(stack) == 0 or x > stack[-1]:
            stack.append(x)
            block += 1
        elif x == stack[-1]:
            pass

    return block


print(solution(H))

