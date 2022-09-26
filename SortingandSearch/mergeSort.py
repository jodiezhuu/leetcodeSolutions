def mergeSort(arr):
    if len(arr) > 1:
        ## find middle index
        mid = len(arr) // 2 # get floor
        ## split array into two halves
        leftArr = arr[:mid]
        rightArr = arr[mid:]
        ## sort subarrays
        mergeSort(leftArr)
        mergeSort(rightArr)
        ## set indices for temp array and left, right array
        i = j = k = 0
        ## append values in temp array
        while i < len(leftArr) and j < len(rightArr):
            if leftArr[i] <= rightArr[j]:
                arr[k] = leftArr[i]
                k += 1
                i += 1
            else:
                arr[k] = rightArr[j]
                k += 1
                j += 1
        ## append left over elements
        while i < len(leftArr):
            arr[k] = leftArr[i]
            k += 1
            i += 1
        while j < len(rightArr):
            arr[k] = rightArr[j]
            k += 1
            j += 1


unorderedArr = [5, 3, 2, 8, 10, 15]
mergeSort(unorderedArr)
print(unorderedArr)