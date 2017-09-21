A = [0, 1, 0, 1, 1]


def solution(A):
    start_flag = 'False'
    total_1_count = 0
    total_0_count = 0
    prefix_1_sum = 0
    for x in A:
        if start_flag == 'True':
            if x == 0:
                total_0_count += 1
                prefix_1_sum = total_1_count + prefix_1_sum
            elif x == 1:
                total_1_count += 1
        elif x == 0:
            start_flag = 'True'
            total_0_count += 1
        else:
            continue
    final = total_0_count * total_1_count - prefix_1_sum
    if final <= 1000000000:
        return final
    else:
        return -1


print solution(A)
