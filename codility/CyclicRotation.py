A = [3, 8, 9, 7, 6]
K = 3

def solution(A, K):
    res = []
    L = len(A)
    for i in range(0,L,1) :
        j = (i + K % L) % L
        res.insert(j, A[i])
    return res

print(solution(A, K))
