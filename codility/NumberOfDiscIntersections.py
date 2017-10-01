A =   [1, 5, 2, 1, 4, 0]

import bisect

def solution(A):

    length = len(A)
    B = [A[i]+i for i in range(len(A))]
    C = [-(A[j]-j) for j in range(len(A))]

    B.sort()
    C.sort()
    cnt = 0

    for x in B:
        position = bisect.bisect_right(C, x)
        cnt += position

    final = cnt - length*(length+1)//2
    if final > 10000000:
        return -1
    else:
        return final


print(solution(A))

#base on the method provided here: https://rafal.io/posts/codility-intersecting-discs.html#fnref1
#discussion on this challenge: https://stackoverflow.com/questions/4801242/algorithm-to-calculate-number-of-intersecting-discs/
#python bisect api: https://stackoverflow.com/questions/4801242/algorithm-to-calculate-number-of-intersecting-discs/
#Binary Search algorithm, which is the algorithm of bisect: http://interactivepython.org/runestone/static/pythonds/SortSearch/TheBinarySearch.html
