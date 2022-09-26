# Binary Search Iteration
# Time Complexity: O(log n) since dividing length by 2
def binarySearchIterate(arr, val):
  high = len(arr) - 1
  low = 0
  while low <= high:
    mid = (low + high) // 2
    if arr[mid] == val:
      return mid
    elif arr[mid] < val:
      low = mid + 1
    else:
      high = mid - 1
  return -1

# Binary Search Recursion
# Time Complexity: O(log n)
def binarySearchRecurse(arr, low, high, val):
  if high >= low:
    mid = low + (high - low) // 2
    if arr[mid] == val:
      return mid
    elif arr[mid] < val:
      return binarySearchRecurse(arr, mid + 1, high, val)
    else: 
      return binarySearchRecurse(arr, low, mid - 1, val)
  else:
    return -1

arr=[2, 4, 8, 10, 12, 14]
print("binary search iteration:", binarySearchIterate(arr, 10))
print("binary search recursion:", binarySearchRecurse(arr, 0, 5, 10))