A = [0,0,0,1,1,0,1,0,0,0,0]

def F_upto_A(L):
    # Fibonacci sequence up to the
    # length of A (include starting and destination position)
    F = []
    F.append(0)
    F.append(1)
    while F[-1] <= L:
        F.append(F[-1]+F[-2])
    return F[1:-1]


def solution(A):
    # add starting position to A
    A.insert(0, 1)
    # add destination position to A
    A.append(1)#[1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1]

    n = len(A)#13

    # store available fibonacci jumps
    F = F_upto_A(n)#[1, 1, 2, 3, 5, 8, 13]

    # S mapping A in position
    # and storing the minimum step count to every "1" position
    S = [n] * n
    S[0] = 0 #[0, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13]
    for i in xrange(1, n):
        # check if the position is 1 in A
        if A[i] == 1 :
            #loop the Fibonacci sequence
            for x in F:
                # previous position
                prev = i - x
                if prev >= 0:
                    # (the minimum step count of the previous position)
                    # plus
                    # (one more step to the existing position)
                    # if less than the step count of the existing position
                    # update the step count of the existing position
                    if S[prev] + 1 < S[i]:
                        S[i] = S[prev] + 1
                else:
                    break

    # return the last position of S, if S[-1]==n ,
    # means destination can'tbe reached
    # S:[0, 13, 13, 13, 13, 1, 13, 2, 13, 13, 13, 13, 3]
    return S[-1] if S[-1] < n else -1



print(solution(A))