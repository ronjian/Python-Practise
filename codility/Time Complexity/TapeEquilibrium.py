import sys

A = [3, 1, 2, 4, 3]
A = [-1000, 1000]


def solution(A):
    min_diff = sys.maxint
    before_P = 0
    after_P = sum(A)
    for P in range(len(A) -1 ):
        before_P += A[P]
        after_P -= A[P]
        diff = abs(before_P - after_P)
        if diff < min_diff:
            min_diff = diff
    if len(A) == 0 :
        return 0
    else:
        return min_diff

print(solution(A))

