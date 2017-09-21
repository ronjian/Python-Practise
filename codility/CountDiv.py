import sys
A = 11
B = 345
K = 17

def solution(A, B, K):
    after_B = B + (K - B%K)
    if A%K == 0:
        before_A  = A - K
    else:
        before_A =  A - A%K
    return (after_B - before_A)/K + 1 -2

print solution(A, B, K)