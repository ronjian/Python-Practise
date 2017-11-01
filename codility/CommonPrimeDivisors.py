# def removeCommonPrimeDivisors(x, y):
#     ''' Remove all prime divisors of x, which also exist in y. And
#         return the remaining part of x.
#     '''
#     while x != 1:
#         gcd_value = gcd(x, y)
#         if gcd_value == 1:
#             # x does not contain any more
#             # common prime divisors
#             break
#         x /= gcd_value
#     return x
#
#
# def hasSamePrimeDivisors(x, y):
#     gcd_value = gcd(x, y)  # The gcd contains all
#     # the common prime divisors
#
#     x = removeCommonPrimeDivisors(x, gcd_value)
#     if x != 1:
#         # If x and y have exactly the same common
#         # prime divisors, x must be composed by
#         # the prime divisors in gcd_value. So
#         # after previous loop, x must be one.
#         return False
#
#     y = removeCommonPrimeDivisors(y, gcd_value)
#
#     return y == 1
#
#
# def solution(A, B):
#     count = 0
#     for x, y in zip(A, B):
#         if hasSamePrimeDivisors(x, y):
#             count += 1
#     return count

#Compute the greatest common divisor.
def gcd(a, b):
    if a % b == 0 :
        return b
    else:
        return gcd(b, a % b)

def checkCommonPrime(e , gcd_value):

    while True:
        new_gcd = gcd(e, gcd_value)
        e /= new_gcd
        #either e is divided to 1
        if e == 1:
            return True
        #either e has some prime can't be divide, than new_gcd will become 1 before e become 1.
        if new_gcd == 1:
            return False


def solution2(A, B):
    count = 0
    for i in range(len(A)):
        gcd_value = gcd(A[i], B[i])

        if checkCommonPrime(A[i], gcd_value):
            if checkCommonPrime(B[i], gcd_value):
                count += 1

    return count



A=[15,10,3]
B=[75,20,6]

print(solution2(A,B))

