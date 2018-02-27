N = 10
M = 4




def solution(N, M ):

    def gcd(N, M):
        if N % M == 0:
            return M
        else:
            return gcd(M, N % M)

    gcd = gcd(N, M)
    return N / gcd  # N / Greatest common dividor


print(solution(N, M))