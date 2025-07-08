def print_path(path):
    for i in path:
        print(i, end=", ")
    print()
def find_path(arr, i, j, path):
    global M,N
    if i == M-1 and j == N-1:
        path.append(arr[i][j])
        print_path(path)
        path.pop()
        return
    if i < 0 or i >= M or j < 0 or j >= N:
        return
    path.append(arr[i][j])
    if j+1<N :
        find_path(arr, i, j+1, path)
    if i+1<M:
        find_path(arr, i+1, j, path)
    path.pop()

if __name__ == "__main__":
    # Input matrix
    arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    # To store the path
    path = []

    # Starting cell (0, 0)
    i, j = 0, 0

    M = len(arr)
    N = len(arr[0])

    # Function call
    find_path(arr,i,j,path)