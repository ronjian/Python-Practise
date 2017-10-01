def quickSort(alist):
    quickSortHelper(alist, 0, len(alist)-1)

def quickSortHelper(alist, first, last):
    if first < last:

        spilitPoint = partition(alist, first, last)

        quickSortHelper(alist, first, spilitPoint-1)
        quickSortHelper(alist, spilitPoint+1, last)

def partition(alist, first, last):
    pivotValue = alist[first]

    leftmark = first+1
    rightmark = last

    done= False
    while not done:

        while alist[leftmark] <= pivotValue and leftmark <= rightmark:
            leftmark += 1

        while alist[rightmark] >= pivotValue and leftmark <= rightmark:
            rightmark -= 1

        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = pivotValue
    alist[first] = alist[rightmark]
    alist[rightmark] = temp

    return rightmark


alist = [54,26,93,17,77,31,44,55,20]
quickSort(alist)
print(alist)
