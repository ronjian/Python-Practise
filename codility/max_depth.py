# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

A = [0,1,3,-2,0,1,0,-3,2,3]

def solution(A):
    # write your code in Python 2.7
    n = len(A)
    l = []
    for Q in range(1, n-1):
        P_d = {}
        Q_d = {}
        for P in range(0, Q ):
            if A[P] - A[Q] > 0 :
                P_d[str(P)+","+str(Q)] = A[P] - A[Q]
        for R in range(Q+1 , n):
            if A[R] - A[Q] > 0 :
                Q_d[str(Q)+","+str(R)] = A[R] - A[Q]
        if len(P_d)>0 and len(Q_d)>0 :
            l.append(min(max(P_d.values()) , max(Q_d.values())))
    if len(l) > 0 :
        return(max(l))
    else :
        return -1


print(solution(A))

# stats = {"a":1 , "b":-10}
# print(stats[(max(stats, key=stats.get))])