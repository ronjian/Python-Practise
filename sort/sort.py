A = [7,3,9,8]

def selectionSort(A):
 n = len(A)
 for k in xrange(n):
  minimal = k
  for j in xrange(k + 1, n):
   if A[j] < A[minimal]:
    minimal = j
  A[k], A[minimal] = A[minimal], A[k] # swap A[k] and A[minimal]
 return A

print(selectionSort(A))


k = 20
def countingSort(A, k):
    n = len(A)
    count = [0] * (k + 1)
    for i in xrange(n):
        count[A[i]] += 1
    p = 0
    for i in xrange(k + 1):
        for j in xrange(count[i]):
            A[p] = i
            p += 1
    return A

print(countingSort(A, k))

def mergeSort(A):
    if len(A)>1:
        mid = len(A)//2
        lefthalf = A[:mid]
        righthalf = A[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                A[k]=lefthalf[i]
                i=i+1
            else:
                A[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            A[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            A[k]=righthalf[j]
            j=j+1
            k=k+1
    return A

print(mergeSort(A))




A.sort()

