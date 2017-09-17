A = [1, 3, 6, 5, 1, 2, -1 ,4]
A = [-1, -3, 0, 2,5]

def solution(A):
    A.sort()
    check = 0
    y = 0
    for x in A:
        if x > 0 and x > y:
            check += 1
            if check <> x:
                return check
        y = x
    return check + 1

print(solution(A))
