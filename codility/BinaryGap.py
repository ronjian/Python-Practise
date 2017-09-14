import re
N = 6291457

def solution(N):
    # write your code in Python 2.7
    B = bin(N)[2:]
    l = re.findall('1*(0+)1+', B)

    max_len = 0

    for s in l:
        lgth = len(s)
        if lgth > max_len:
            max_len = lgth

    return max_len

print(solution(N))