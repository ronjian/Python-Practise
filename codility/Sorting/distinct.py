A = [2, 1, 1, 2, 3, 1]
A = []
A = [-1, -2 ,-6, 5,0, -10, -1]


def solution(A):

    d = {}

    for x in A:
        if d.has_key(x):
            d[x] += 1
        else:
            d[x] = 1

    final = len(d.keys())

    return final


print(solution(A))

