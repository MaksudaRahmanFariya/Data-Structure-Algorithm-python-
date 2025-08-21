def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        flag = 0
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                flag = 1
        if flag == 0:
            break
    return arr
if __name__ == "__main__":
    arr = [5,2,6,4,3,9,1]
    print(bubble_sort(arr))