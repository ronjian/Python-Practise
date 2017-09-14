A = [1, 3, 6, 4, 1, 2,7, 5]
B = [-5,-6,-9]
C = [1,2,3,6,7,8,100]
D = [-10,-9,0,1,13,100]

def solution(A):
    A.sort(reverse = 1)
    min = A.pop()
    def min_loop(A, min):
        if len(A) > 0:
            next = A.pop()
            if next - min > 1 and min >=0:
                return min + 1
            else:
                min = next
                return min_loop(A, min)
        elif min < 0 : return 1
        else : return min + 1

    return min_loop(A, min)

print(solution(A))
print(solution(B))
print(solution(C))
print(solution(D))
