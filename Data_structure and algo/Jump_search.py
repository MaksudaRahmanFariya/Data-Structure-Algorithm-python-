import math


def jump_search(arr, n, key):
    # block size
    step = math.sqrt(n)
    #finding the block where the key is
    prev = 0
    while arr[int(min(step, n)-1)] < key:
        prev = step
        step += math.sqrt(n)
        if prev >= n:
            return -1
    #linear search for key
    while arr[int(prev)] < key:
        prev += 1
        if prev == min(step, n):
            return -1
    if arr[int(prev)] == key:
        return prev
    return -1
if __name__ == "__main__":
    arr = [0, 1, 1, 2, 3, 5, 8, 13, 21,
           34, 55, 89, 144, 233, 377, 610]
    n = len(arr)
    key = 55
    index = jump_search(arr, n, key)
    print("Number of ", key, "is at index","%.0f" %index)



