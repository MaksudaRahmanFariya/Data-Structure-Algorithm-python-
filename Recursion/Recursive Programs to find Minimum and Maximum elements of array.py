def minimumandmax(n,idx,mini,maxi):
    if idx == len(n):
        return mini, maxi
    if n[idx] > maxi:
        maxi = n[idx]
    if n[idx] < mini:
        mini = n[idx]

    return minimumandmax(n, idx + 1, mini, maxi)

    #minimumandmax(n,idx+1,mini,maxi)



if __name__ == "__main__":
    n = [-5,6,-10,15,4,7,8]
    mini, maxi = minimumandmax(n,0,float('inf'), float('-inf'))
    print(mini)
    print(maxi)

