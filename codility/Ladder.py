
B = [3,2,4,3,1,3,4,5]
A = [1,2,3,4,5,6,7,8]

#from scipy.special import comb
from math import factorial

def solution(A, B):

    C = [0]*len(A)
    for i in range(len(A)):
        count = 1
        j = 1
        while 2*j<= A[i]:
            length = A[i] - 2*j + j
            #count += comb(length, j)
            count += factorial(length) / factorial(j) / factorial(length - j)
            j += 1

        C[i] = count % 2**B[i]

    return C

print(solution(A, B))

#https://codesays.com/2014/solution-to-ladder-by-codility/
def solution2(A, B):

    #prepare Fibonacci numbers
    L = max(A)
    F = [0] * (L+2)
    F[1] = 1
    for j in range(2,L+2):
        F[j] = (F[j-1] + F[j-2])

    result = [0] * len(A)
    for i in range(len(A)):
        #C[i] = F[A[i] + 1] % 2**B[i]
        #C[i] = F[A[i]+1] % (1<<B[i])
        #bitwise :https://wiki.python.org/moin/BitwiseOperators
        result[i] = F[A[i] + 1] & ( (1 << B[i]) - 1 )
        #2^i = 1<<i
        #n % 2^i = n & (2^i - 1)
        #https://stackoverflow.com/questions/3072665/bitwise-and-in-place-of-modulus-operator

    return result

print(solution2(A, B))


