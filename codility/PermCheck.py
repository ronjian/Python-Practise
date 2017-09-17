A = [4, 1, 3]
A = [4, 1, 3, 2]
A = []
# A = [9, 5, 7, 3, 2, 7, 3, 1, 10, 8]

def solution(A):
    A.sort()
    check = 1
    for x in A:
        if x <> check:
            return 0
        check += 1
    if len(A)>0 :
        return 1
    else :
        return 0

print(solution(A))