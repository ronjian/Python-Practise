
def solution(N, P, Q):
    import math


    N_l = [0]*(N+1)

    i = 2

    while (i*i <= N ):
        k = i*i
        while (k<=N):
            log = round(math.log(k,i))
            if i**log == k :
                N_l[k] += log
            else:
                N_l[k] +=2
            k += i
        i += 1


    sum = 0
    for i in range(len(N_l)):
        if N_l[i] == 2 :
            sum += 1
        N_l[i] = sum


    M = []
    for i in range(len(P)):
        M.append((N_l[Q[i]] - N_l[P[i]-1]))


    return M


def solution2(N, P, Q):
    from math import sqrt

    # Find out all the primes with Sieve of Eratosthenes
    prime_table = [False] * 2 + [True] * (N - 1)
    prime = []
    prime_count = 0
    for element in xrange(2, int(sqrt(N)) + 1):
        if prime_table[element] == True:
            prime.append(element)
            prime_count += 1
            multiple = element * element
            while multiple <= N:
                prime_table[multiple] = False
                multiple += element
    for element in xrange(int(sqrt(N)) + 1, N + 1):
        if prime_table[element] == True:
            prime.append(element)
            prime_count += 1

    # Compute the semiprimes information
    semiprime = [0] * (N + 1)
    # Find out all the semiprimes.
    # semiprime[i] == 1 when i is semiprime, or
    #                 0 when i is not semiprime.
    for index_former in xrange(prime_count - 1):
        for index_latter in xrange(index_former, prime_count):
            if prime[index_former] * prime[index_latter] > N:
                # So large that no need to record them
                break
            semiprime[prime[index_former] * prime[index_latter]] = 1
    # Compute the number of semiprimes until each position.
    # semiprime[i] == k means:
    # in the range (0,i] there are k semiprimes.
    for index in xrange(1, N + 1):
        semiprime[index] += semiprime[index - 1]

    # the number of semiprimes within the range [ P[K], Q[K] ]
    # should be semiprime[Q[K]] - semiprime[P[K]-1]
    question_len = len(P)
    result = [0] * question_len
    for index in xrange(question_len):
        result[index] = semiprime[Q[index]] - semiprime[P[index] - 1]


    return result



P = [1,4,16]
Q = [26,10,20]


N = 1000000
P = [1]
Q = [1000000]

A = solution(N,P,Q)
B = solution2(N,P,Q)
print(A)
print(B)

# for i in range(len(A)):
#     if A[i] != B[i]:
#         print i
#         break


# python float precise issue:
# >>> import math
# >>> print(math.log(125,5))
# 3.0000000000000004



