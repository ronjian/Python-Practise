N = 30

def solution(N):

    i = 1
    perimeter = -1
    while i * i <= N:
        if N % i == 0 :
            current = 2 * (i + N/i)
            if perimeter == -1 or current < perimeter:
                perimeter = current
        i += 1

    return perimeter


print(solution(N))

