def quicksort(arr, low,high):
    if low >= high:
        return
    s = low
    e = high
    m = s + (e-s)//2
    pivot = arr[m]
    while s <= e:
        while arr[s] < pivot:
            s += 1
        while arr[e] > pivot:
            e -= 1
        if s <= e:
            temp = arr[s]
            arr[s] = arr[e]
            arr[e] = temp
            s +=1
            e -=1
    quicksort(arr,low,e)
    quicksort(arr,s,high)

if __name__ == "__main__":
    arr = [5,4,3,2,1]
    quicksort(arr,0,len(arr)-1)
    print(arr)

