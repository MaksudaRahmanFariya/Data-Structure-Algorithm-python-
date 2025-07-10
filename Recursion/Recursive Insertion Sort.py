def merge_sort(arr,idx):
    if idx == len(arr):
        return arr
    for i in range(0,idx):
        if arr[i]>arr[idx]:
            arr[i],arr[idx] = arr[idx],arr[i]
    return merge_sort(arr,idx+1)
if __name__ == "__main__":
    arr = [9,7,6,15,17,5,10,11]
    print(merge_sort(arr,1))

