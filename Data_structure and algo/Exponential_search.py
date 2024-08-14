import math
def binary_search(arr, l, r, key):
    if r >= l :
        mid = l + (r-l)//2
        if arr[mid] == key:
            return mid
        if arr[mid] > key:
            return binary_search(arr, l, mid-1, key)
        return binary_search(arr, mid+1, r, key)
    return -1
def exponentialsearch(arr,n,key):
    if arr[0] == key:
        return 0
    i = 1
    while i < n and arr[i] <= key:
        i = i*2
    return binary_search(arr, i//2, min(i,n-1), key)
if __name__ == "__main__":
    arr = [2, 3, 4, 10, 40]
    n = len(arr)
    x = 10
    result = exponentialsearch(arr, n, x)
    if result == -1:
        print("Element not found in the array")
    else:
        print("Element is present at index %d" % (result))

