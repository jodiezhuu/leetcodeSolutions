# Time Complexity: O(n * log n)
# Space Complexity: O(log n)
def partition(array, low, high):
    pivot = array[high] # right most element as pivot
    i = low - 1 # pointer for greater element 
    for j in range(low, high): # compare each element with pivot val
        if array[j] <= pivot:
            i += 1 # swap with greater element (i)
            tmp = array[i] # swap element at i with j
            array[i] = array[j]
            array[j] = tmp
    # swap pivot element with greater element 
    tmp = array[i + 1]
    array[i + 1] = array[high]
    array[high] = tmp
    # return partition index
    return i + 1

def quickSort(array, low, high):
    if low < high:
        par = partition(array, low, high)
        quickSort(array, low, par - 1) # repeat on left of pivot
        quickSort(array, par + 1, high) # repeat on right of picot 

data = [3, 2, 5, 1, -9, 29, 18]
quickSort(data, 0, len(data) - 1)
print(data)