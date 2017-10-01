A = [-3, 1, 2, -2, 5, 6]

def solution(A):

    if len(A) >= 3:

        A.sort()

        last = len(A) -1
        last_three = A[last] * A[last -1] * A[last-2]

        # if A[0] >= 0 or (A[0] < 0 and A[1] >= 0):
        #     return last_three
        # elif A[-1:] < 0:
        #     return last_three
        # elif A[0] < 0 and A[1] <0 and A[-1:] >=0:
        #     return max(last_three, A[0] * A[1] * A[-1:])

        return max(last_three, A[0] * A[1] * A[last])

    return -1



print(solution(A))

