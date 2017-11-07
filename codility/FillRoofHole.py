
def solution(A, k):
    n = len(A)
    start = 0
    end = n-1
    size = -1
    while (start <= end):
        mid = (start + end) / 2
        #find the first matching element here
        if (CheckBoardsCount(A, mid) > k):
            start = mid + 1
        else:
            end = mid - 1
            size = mid


    return size

def CheckBoardsCount(A, size):
    n = len(A)
    count = 0
    last = -1
    for i in xrange(n):
        if A[i] == 1 and last < i:
            count += 1
            last = i + size - 1

    return count


A = [0,1,0,1,0,0,0,0,1,1,0,1]
k = 3
print(solution(A, k))
k = 4
print(solution(A, k))
k = 2
print(solution(A, k))
