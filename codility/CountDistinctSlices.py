def SumOFArithmeticProgression (n):
    return (1+n) * n // 2

def distance(end, head):
    return head - end + 1

def solution(M, A):


    L = len(A)
    #index of stock represent the number from A
    #value of stock represent the location of the number from A
    stock = [-1]*(M+1)
    end = 0 # end of the current slice
    n = 0
    overlap_slice_length = 0

    for head in xrange(0,L):
        value = A[head]


        # current slice is A[end:head+1]
        # not exist in current slice
        if stock[value] < end or head == 0:
            pass
        #find duplicate number, which already exists in current slice
        else:
            #shrink the slice to None, the combination of the length
            n += SumOFArithmeticProgression(current_slice_length)
            #update the end
            end = stock[value] + 1
            overlap_slice_length = distance(end, head - 1)
            #overlap with next time shrink
            n -= SumOFArithmeticProgression(overlap_slice_length)

        #update the location of new value
        stock[value] = head

        current_slice_length = distance(end, head)


    #last shrink
    n += SumOFArithmeticProgression(current_slice_length)

    return min(n, 1000000000)


def solution2(M, A):
    accessed = [-1] * (M + 1)  # -1: not accessed before
    # Non-negative: the previous occurrence position
    front, back = 0, 0
    result = 0

    for front in xrange(len(A)):
        if accessed[A[front]] == -1:
            # Met with a new unique item
            accessed[A[front]] = front
        else:
            # Met with a duplicate item
            # Compute the number of distinct slices between newBack-1 and back
            # position.
            newBack = accessed[A[front]] + 1
            result += (newBack - back) * (front - back + front - newBack + 1) / 2
            if result >= 1000000000:   return 1000000000

            # Restore and set the accessed array
            for index in xrange(back, newBack):
                accessed[A[index]] = -1
            accessed[A[front]] = front

            back = newBack

    # Process the last slices
    result += (front - back + 1) * (front - back + 2) / 2

    return min(result, 1000000000)

from random import randint
M = 100
while True:
    A = [randint(0, M) for x in xrange(M)]
    if solution(M,A) <> solution2(M,A) :
        print(A)
        break
