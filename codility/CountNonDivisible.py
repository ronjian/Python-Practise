A = [3,1,2,3,6]
# A = [1, 2, 3, 4, 2, 32, 1, 21, 2, 33, 23, 123, 1, 21312, 2, 3, 213, 13, 12, 3, 123, 213, 932742]
# A = [3,4]


def solution(A):

    N = len(A)
    m = max(A)

    M = {}
    for x in A:
        if M.has_key(x):
            M[x][0] += 1
        else:
            M[x] = [1,0]


    for i in range(2, m+1 ):
        if M.has_key(i):
            j = i
            while j <= m:
                if M.has_key(j) :
                    M[j][1] += M[i][0]
                j += i

    for i in range(len(A)):
        A[i] = N - M[A[i]][1] - M.get(1,[0,0])[0]

    return A



print(solution(A))

