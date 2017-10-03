A = [4, 3, 2, 1, 5]
B = [0, 1, 0, 0, 0]

def solution(A, B):

    stack = []
    for i in range(len(B)):
        if len(stack) == 0:
            stack.append(i)
        else:
            while len(stack) != 0 and B[i] - B[stack[-1]] == -1 and A[stack[-1]] < A[i]:
                stack.pop()
            if len(stack) != 0:
                if B[i] - B[stack[-1]] != -1:
                    stack.append(i)
            else:
                stack.append(i)

    return(len(stack))


print(solution(A, B))


