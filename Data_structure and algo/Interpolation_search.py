import math
def interpolationSearch(arr, hi, lo, key):
    if (lo <= hi and key >= arr[lo] and key <= arr[hi]) :
        # uniform distribution in mind
        pos = lo + ((hi-lo)//(arr[hi] - arr[lo])*(key-arr[lo]))
        if arr[pos] == key:
            return pos
        if arr[pos] < key:
            return interpolationSearch(arr, hi, pos+1, key)
        if arr[pos] > key:
            return interpolationSearch(arr, pos-1, lo, key)
    return -1

if __name__ == "__main__":
    arr = [10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47]
    hi = len(arr)
    key = 21
    index = interpolationSearch(arr, hi - 1,0, key)
    if index != -1:
        print("index of element is", index)
    else:
        print("element is not found")






