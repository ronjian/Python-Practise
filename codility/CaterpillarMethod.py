#  https://codility.com/media/train/13-CaterpillarMethod.pdf
def example(A, S):
    total = A[0]
    i = 0
    n = len(A)
    for j in xrange(n):
        while i < n:
            i += 1
            total += A[i]

            if total == S :
                return A[j:i+1]
            elif total < S :
                pass
            else :
                break

        total -= A[j]

    return -1

A = [6,2,7,4,1,3,6]
S = 12
print(example(A, S))


def execise(B):
    n = len(B)
    result = 0
    for x in xrange(n):
        z=x+2
        for y in xrange(x + 1, n):
            while (z < n and B[x] + B[y] > B[z]):
                z += 1
            result += z - y - 1
    return result

B = [3,3,3,3]
print(execise(B))


