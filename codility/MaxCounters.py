A = [3 ,4, 4, 6, 1, 4, 4]
N = 5

# def solution(N, A):
#     final = [0]*N
#     max_value = 0
#     for X in A:
#         if 1<= X and X <= N:
#             final[X - 1] += 1
#             if final[X - 1] > max_value:
#                 max_value = final[X - 1]
#         if X == N + 1:
#             final = [max_value]*N
#     return final

def solution(N, A):
    stack = [[0,0] for i in range(N)] #[value, batch_count]
    max_value = 0
    batch_count = 0
    batch_value = 0
    after_batch = 'False'

    for X in A:
        #increase mode
        if 1 <= X <= N:
            #catch up the batch: 1. after batch mode, 2.batch hasn't catch up before
            if after_batch == 'True' or stack[X - 1][1] <> batch_count:
                stack[X - 1][0] = 1
                stack[X - 1][1] = batch_count
            #increase on current batch
            else:
                stack[X - 1][0] +=1
            #figure out the max value
            if stack[X - 1][0] + batch_value > max_value:
                max_value = stack[X - 1][0] + batch_value
            #after batch indicator
            after_batch = 'False'
        #batch mode
        elif X == N + 1:
            batch_count += 1
            batch_value = max_value
            after_batch = 'True'
    #final list
    final = [0] * N
    for i in range(len(stack)):
        # catch up the batch: 1. after batch mode, 2.batch hasn't catch up before
        if after_batch == 'True' or stack[i][1] <> batch_count:
            final[i] = batch_value
        # increase on current batch
        else :
            final[i] = batch_value + stack[i][0]

    return final

#simplize:
def solution2(N, A):
    final= [0 for i in range(N)]
    batch_value = 0
    max_value = 0
    for X in A:
        if 1 <= X <= N:
            final[X-1] = max(batch_value+1 , final[X-1]+1)
            max_value = max(final[X-1], max_value)
        elif X == N+1:
            batch_value = max_value
    for i in range(len(final)):
        final[i] = max(final[i], batch_value)
    return final


#print(solution(N, A))
print(solution2(N, A))

