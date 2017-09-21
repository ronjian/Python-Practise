A = [0,1,2,2,3,5]
B = [500000,500000,0,0,0,20000]

A = [0, 0]
B = [0, 0]

def solution(A, B):
    C = [0]*len(A)
    count = 0
    D = []
    for i in range(len(A)):
        C[i] = A[i] + B[i]/float(1000000)
        for j in range(0,i):
            if C[j] * C[i]>= C[j] + C[i]:
                count += 1
                D.append((j,i))
    print(C)
    print D
    return count





print(solution(A, B))