def find_first_nail(x, y , nail_sort, prev_result):

    # plank is out of the range of nails
    if nail_sort[0][1] > y or nail_sort[-1][1] < x :
        return -1

    # binary search the start position
    L = len(nail_sort)
    s = 0
    e = L-1

    pos = -1
    while s <= e:
        mid = (s+e)/2
        if nail_sort[mid][1] < x :
            s = mid+1
        # elif nail_sort[mid][1] > y :
        #     e = mid - 1
        else :
            e = mid - 1
            pos = mid

    # Cannot find one to nail the plank
    if pos == -1: return -1

    result = nail_sort[pos][0]

    pos += 1
    while pos < L:
        # if out bound of the range of nail, then stop loop
        if nail_sort[pos][1] > y:
            break
        # minimize
        result = min(nail_sort[pos][0],result)
        pos += 1
        # if previous necessary nail position is already
        # larger than the existing required nail position
        # , then break the loop and return previous position
        if prev_result >= result:
            return prev_result

    # if result is at the last position of nail_sort,
    # then previous result is necessary to compare
    return max(prev_result ,result)


def solution(A, B, C):
    nail_sort = sorted(enumerate(C, start=1),key=lambda x : x[1])
    result = -1
    for x, y in zip(A, B):
        result = find_first_nail(x, y , nail_sort, result)
        if result == -1 :
            return -1

    return  result


def solution2(A, B, C):
    result = -1  # Global result

    # Sort the planks according to firstly their begin position,
    # and then their end position
    planks = zip(A, B)
    planks.sort()

    # Sort the nails according to their position
    nails = sorted(enumerate(C), key=lambda x: x[1])
    nailsIndex = 0

    # Travel for each plank
    for plankIndex in xrange(len(planks)):
        plank = planks[plankIndex]

        # Find the first qualified nail in linear manner. Beware
        # that the planks are sorted. For any two adjacent planks,
        # the begin position of the latter one will be:
        #   either the same as the former's begin position
        #   or after the former's
        # In both cases, the nails, which before the nailsIndex
        # of the former plank's round, would never be candidates
        # in the latter plank's round. Thus we only need to search
        # nails from the previous nailsIndex position.
        while nailsIndex < len(nails):
            if nails[nailsIndex][1] < plank[0]:
                nailsIndex += 1
            elif nails[nailsIndex][1] > plank[1]:
                # And all the remaining nails > plank[1]
                # Impossible to find a qualified nail
                return -1
            else:
                # plank[0] <= nails[nailsIndex][1] <= plank[1]
                break
        else:
            # Cannot find one
            return -1

        if plankIndex != 0 and plank[0] == planks[plankIndex - 1][0]:
            # This plank and previous plank have the same begin
            # position. And the planks are sorted. So the end
            # position of this plank is after that of previous
            # plank. We continue the previous search.
            pass
        else:
            # This plank and previous plank have the different
            # begin position. We have to re-search from the
            # nailsIndex.
            tempRes = len(nails)  # Local result for this round
            tempIndex = nailsIndex

        # Find the first one in all the qualified nails
        while tempIndex < len(nails) and plank[0] <= nails[tempIndex][1] <= plank[1]:
            tempRes = min(tempRes, nails[tempIndex][0])
            tempIndex += 1
            # If we find a tempRes <= result, the final result
            # of current round will <= result. This tempRes
            # would never change the global result. Thus we
            # could ignore it, and continue the next round.
            if tempRes <= result:   break

        result = max(result, tempRes)

    return result + 1

A = [1,4,5,8]
B = [4,5,9,10]
C = [2,2,2,2,5,8,2,2,2,2]
# A = [2]
# B = [2]
# C = [3]
print(solution(A, B, C))
print(solution2(A, B, C))

# x =10
# y =11
# nail_sort=[(5, 2), (1, 4), (2, 6), (3, 7), (4, 10)]
# print(find_first_nail(x, y , nail_sort))
