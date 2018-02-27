A = [1,3,1,4,2,3,5,4]
X = 5

# def solution(X, A):
#     B = list(range(1, X+1, 1))
#     for i in range(0, len(A), 1):
#         if A[i] <= X :
#             try:
#                 B.remove(A[i])
#             except ValueError:
#                 pass
#         if len(B) == 0:
#             return i
#     return -1

# def solution(X, A):
#     B = list(range(1, X + 1, 1))
#     max_idx = 0
#     for E in B:
#         try:
#             idx = A.index(E)
#         except ValueError:
#             return -1
#         if idx > max_idx:
#             max_idx = idx
#     return max_idx

#O(N)
def solution(X, A):
    Indicator = ['unfound']*X
    found_cnt = 0
    for i in range(len(A)):
        value = A[i]
        if value <= X and Indicator[value-1] == 'unfound':
            Indicator[value - 1] = 'found'
            found_cnt += 1
        if found_cnt == X:
            return i
    return -1


print(solution(X, A))