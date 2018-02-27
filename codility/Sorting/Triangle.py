A = [10, 2, 5, 1, 8, 20]
A = [2,3,8]

def solution(A):

    if len(A) < 3:
        return 0

    A.sort()

    for i in range(0,len(A)-2):
        if A[i] + A[i+1] > A[i+2]:
            return 1

    return 0


print(solution(A))

