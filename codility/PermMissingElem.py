A = [2, 3, 1, 5]
A = []
A = [1,2,3]

def solution(A):
    l = len(A)
    should_be = (1 + (l + 1)) * (l + 1) / 2
    now_is = sum(A)
    return should_be - now_is


print(solution(A))