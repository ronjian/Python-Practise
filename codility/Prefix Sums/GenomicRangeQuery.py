# P = [2,5,0]
# Q = [4,5,6]
# S = 'CAGCCTA'
# #[2, 4, 1]

P = [0,0,1]
Q = [0,1,1]
S = 'AC'
#[1, 1, 2]

# P = [0, 0, 1]
# Q = [0, 1, 1]
# S = 'GT'
# #[3, 3, 4]


def solution(S, P, Q):
    prefix_element_d = []
    for i in range(len(S)):
        if i == 0 :
            new_dict = {'A':0, 'C':0, 'G':0, 'T':0}
            new_dict[S[i]] = 1
            prefix_element_d.append(new_dict)
        else:
            new_dict = dict.copy(prefix_element_d[i-1])
            new_dict[S[i]] += 1
            prefix_element_d.append(new_dict)

    final = [0 for x in range(len(P))]

    value_dict = {'A':1, 'C':2, 'G':3, 'T':4}
    for j in range(len(P)):
        if Q[j] == P[j] :
            final[j] = value_dict[S[P[j]]]
        else:
            value_l = []
            for k, v in prefix_element_d[Q[j]].items():
                if (P[j] == 0 and v > 0) or ( P[j] >= 1 and v - prefix_element_d[P[j] - 1][k] > 0 ):
                    value_l.append(value_dict[k])
            if len(value_l) == 0:
                final[j] = 0
            else:
                final[j] = min(value_l)
    return final

print(solution(S, P, Q))



