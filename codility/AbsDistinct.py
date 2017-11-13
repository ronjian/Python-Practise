
#Caterpillar method
def solution1(A):
    neg = filter(lambda x: x <0 , A)[::-1]
    pos = filter(lambda x: x >=0 , A)

    n = 0
    j = 0
    pos_last = None
    neg_last = None
    pos_l = len(pos)
    neg_l = len(neg)
    for i in xrange(pos_l):
        if pos_last != pos[i] and pos[i] != neg_last :
            n += 1
        pos_last = pos[i]

        while j < neg_l and (abs(neg[j]) <= pos_last or i == (pos_l - 1)) :
            if abs(neg[j]) != pos_last and neg[j] != neg_last :
                n += 1
            neg_last = neg[j]
            j += 1

    if pos_l == 0 :
        for j in xrange(neg_l):
            if neg[j] != neg_last:
                n += 1
            neg_last = neg[j]

    return n

def find_mid(A, x):
    n = len(A)
    start = 0
    end = n-1
    result = -1
    while (start <= end):
        mid = (start + end)/2
        if A[mid] < x:
            start = mid + 1
        else:
            end = mid - 1
            result = mid #this follow with equal condition

    return result

def solution2(A):
    mid = find_mid(A, 0)
    L = len(A)
    last_neg = None
    last_pos = None
    n = 0
    right = mid
    left = mid -1
    if mid == -1 or mid == 0: #all negtive, or all positive
        last = None
        for i in xrange(L):
            if A[i] != last:
                n+=1
            last=A[i]
    else:
        while left >= 0 or right <= L -1:
            if right <= L -1 and (abs(A[left]) >= A[right] or left == 0):
                if A[right] <> last_pos and A[right]  <> last_neg:
                    n+=1
                last_pos = A[right]
                right +=1
            else:
                if A[left] <> last_neg and abs(A[left]) <> last_pos:
                    n+=1
                last_neg = A[left]
                left -=1

    return n


def solution3(A):
    abs_distinct = 1
    current = max(abs(A[0]), abs(A[-1]))
    index_head = 0
    index_tail = len(A) - 1

    while index_head <= index_tail:
        # We travel the array from the greatest
        # absolute value to the smallest.

        former = abs(A[index_head])
        if former == current:
            # Skip the heading elements, whose
            # absolute values are the same with
            # current recording one.
            index_head += 1
            continue

        latter = abs(A[index_tail])
        if latter == current:
            # Skip the tailing elements, whose
            # absolute values are the same with
            # current recording one.
            index_tail -= 1
            continue

        # At this point, both the former and
        # latter has different absolute value
        # from current recorded one.
        if former >= latter:
            # The next greatest value is former
            current = former
            index_head += 1
        else:
            # The next greatest value is latter
            current = latter
            index_tail -= 1

        # Meet with a new absolute value
        abs_distinct += 1

    return abs_distinct


A = [-5,-3,-1,0,3,6]
# A = [-1,0]
# A = [-1,0,1]
# A = [0, 1, 2, 3]
# A = [1,1]
# A = [-2,-1,3,4,5]
# A = [-10]
# A = [1]
# print(solution1(A))
# print(solution2(A))
print(solution3(A))
