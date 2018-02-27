def block_at_least(A, max_size):
    accumulate = 0
    blocks = 1
    for x in A:
        accumulate += x
        if accumulate > max_size:
            accumulate = x
            blocks += 1

    return blocks


def solution(K, M, A):
    S = sum(A)
    start = max(S / K, max(A))
    end = S

    result = S # at first, suppose only one block
    while start <= end:
        mid = (start + end)/2
        if block_at_least(A, mid) <= K:
            # at this max size,
            # the block count is less than the given K,
            #  then the max size can be less
            end = mid - 1
            result = mid
        else :
            start = mid + 1

    return  result


A = [4,4]
K = 2
M = 10

print(solution(K, M, A))