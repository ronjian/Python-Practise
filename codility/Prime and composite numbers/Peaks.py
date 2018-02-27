import random

def solution(A):

    N = len(A)

    peak = []
    level = 0
    for i in range(N):
        peak.append(level)
        if 0<i<N-1 and A[i-1] < A [i] and A[i] > A[i+1]:
            level += 1

    dividor = []
    j = 1
    while j * j <= N:
        if N % j == 0 and j*j != N :
            dividor.append(j)
            dividor.append(N//j)
        elif j*j == N:
            dividor.append(j)
        j += 1

    dividor.sort()

    if N >=3:
        for x in dividor:
            if x == N:
                if len(peak) > 0 and peak[0] != peak[-1] : return 1
            else:
                if peak[x] == 0:
                    continue

                z=x
                flg=True
                while z < N:
                    if peak[z] > peak[z-x]:
                        z = z + x
                    else:
                        flg = False
                        break

                if z == N and peak[z - 1] == peak[z - x]:
                    flg = False

                if flg == True: return N//x

    return 0



def solution2(data):

    length = len(data)

    # array ends can't be peaks, len < 3 must return 0
    if len < 3:
        return 0

    peaks = [0] * length

    # compute a list of 'peaks to the left' in O(n) time
    for index in range(2, length):
        peaks[index] = peaks[index - 1]

        # check if there was a peak to the left, add it to the count
        if data[index - 1] > data[index - 2] and data[index - 1] > data[index]:
            peaks[index] += 1

    # candidate is the block size we're going to test
    for candidate in range(3, length + 1):

        # skip if not a factor
        if length % candidate != 0:
            continue

        # test at each point n / block
        valid = True
        index = candidate
        while index != length:

            # if no peak in this block, break
            if peaks[index] == peaks[index - candidate]:
                valid = False
                break

            index += candidate

        # one additional check since peaks[length] is outside of array
        if index == length and peaks[index - 1] == peaks[index - candidate]:
            valid = False

        if valid:
            return length / candidate

    return 0

A = [1, 2, 3]
print(solution(A))
# print(solution2(A))

# while True:
#     A = [int(1000*random.random()) for i in xrange(10000)]
#     s1 = solution(A)
#     s2 = solution2(A)
#     if s1 != s2:
#         print(A)
#         print(s1)
#         print(s2)
#         break


