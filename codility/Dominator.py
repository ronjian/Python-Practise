A = [3,4,3,2,3,-1,3,3]

def solution(A):

    stack = []

    #seek candidate, putting in stack[-1]
    for x in A:
        if len(stack) == 0:
            stack.append(x)
        elif stack[-1] != x:
            stack.pop()
        else:
            stack.append(x)

    # identify dominator
    count = 0
    if len(stack) != 0:
        indices = []
        for i in range(len(A)):
            if A[i] == stack[-1]:
                indices.append(i)
                count += 1

    if count * 2 > len(A):
        return indices[0]
    else:
        return -1


print(solution(A))

