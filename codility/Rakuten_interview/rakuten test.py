A = [1, 8, -3,0,1,3,-2,4,5]
A=[2]
A=[3]
A=[3,3]
A=[3,3,3]
K = 6

def solution(K , A):

    d = {}
    for x in A:
        d[x] = d.get(x,0) + 1

    count = 0
    for x in A:
        count += d.get(K-x, 0)

    return count

print(solution(K,A))

