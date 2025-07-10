def recursion(arr,n,idx):
    if idx == n-1:
        return
    for i in range(idx,n-1):
        if arr[idx]>arr[idx+1]:
            arr[idx],arr[idx+1] = arr[idx+1],arr[idx]
        recursion(arr,n,idx+1)
    return arr

def show(arr):
    n = len(arr)
    recursion(arr,n,0)
    return arr
if __name__ == "__main__":
    arr = [10,5,3,9,1]
    ans = recursion(arr,len(arr),0)
    print(ans)
    #print(show(arr))

