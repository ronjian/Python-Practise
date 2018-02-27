A = [4,3,4,4,4,2]
A = []


def solution(A):

    length = len(A)
    candidate = []
    lead = None
    equi_cnt = 0

    #seek candidate
    for x in A:
        if len(candidate) == 0:
            candidate.append(x)
        elif candidate[-1] != x:
            candidate.pop()
        else:
            candidate.append(x)

    count = 0
    if len(candidate) > 0:
        for x in A:
            if x == candidate[-1]:
                count += 1

    #identify lead
    if count * 2 > length:
        lead = candidate[-1]

    #identify lead after spiliting
    if lead is not None:
        before_count = 0
        for i in range(len(A)):
            before = i+1
            after = length - (i+1)
            if A[i] == lead: before_count += 1
            if before_count * 2 > before and (count - before_count) * 2 > after:
                equi_cnt += 1

    return equi_cnt



print(solution(A))


