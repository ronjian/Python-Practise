A = [12,15,15,15,16,19,59,59,60]

def find_last(A, x):
    n = len(A)
    start = 0
    end = n-1
    result = -1
    while (start <= end):
        mid = (start + end)/2
        if A[mid] <= x:
            start = mid + 1
            result = mid #this follow with equal condition
        else:
            end = mid - 1

    # return result
    return result if A[result] == x else -1

print(find_last(A, 15))#3
print(find_last(A, 59))#7
print(find_last(A, 59.1))#-1
#this will always find the last matching element


def find_first(A, x):
    n = len(A)
    start = 0
    end = n-1
    result = -1
    while (start <= end):
        mid = (start + end)/2
        if A[mid] < x:
            start = mid + 1
        else:
            end = mid - 1
            result = mid #this follow with equal condition

    # return result
    return result if A[result] == x else -1

print(find_first(A, 15))#1
print(find_first(A, 59))#6
print(find_first(A, 59.1))#-1
#this will always find the first matching element
