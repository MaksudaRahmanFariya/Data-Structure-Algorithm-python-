import math
def max_value(arr, lo, high):
    if lo>high:
        return float('-inf')
    if lo == high:
        return arr[lo]
    mid = (lo+high)//2
    left_max = max_value(arr,lo,mid)
    right_max = max_value(arr, mid+1, high)
    return max(left_max, right_max)



