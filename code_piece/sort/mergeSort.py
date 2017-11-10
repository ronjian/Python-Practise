A = [28,9,19,15,20,1]

def mergeSort(A):
    #spliting
    if len(A) > 1:
        half = len(A) // 2
        left_half = A[:half]
        right_half = A[half:]
        
        mergeSort(left_half)
        mergeSort(right_half)

        #merging
        i = 0
        j = 0
        k = 0
        while i < len(left_half) and j < len(right_half) :
            if left_half[i] < right_half[j]:
                A[k] = left_half[i]
                i += 1
            else:
                A[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            A[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            A[k] = right_half[j]
            j += 1
            k += 1

mergeSort(A)
print(A)
