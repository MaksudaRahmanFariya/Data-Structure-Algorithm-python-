import math
def partition(arr, low, high):
    pivot = arr[high]
    i = low-1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1
def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr,low,high)
        quick_sort(arr,low,pi-1)
        quick_sort(arr, pi+1, high)
def print_arr(arr):
    for i in arr:
        print(i, end=" ")
    print()

if __name__ == "__main__":
    arr = [10, 7, 8, 9, 1, 5]
    print("Given array is")
    print_arr(arr)

    quick_sort(arr,0, len(arr) - 1)

    print("\nSorted array is")
    print_arr(arr)

