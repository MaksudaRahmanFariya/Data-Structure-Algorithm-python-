def nai(n):
    if len(n) < 1:
        return
    temp = [0]*(len(n)-1)
    for i in range(0,len(n)-1):
        x = n[i]+n[i+1]
        temp[i] = x
    nai(temp)
    print(n)
if __name__ == '__main__':
    n = [1,2,3,4,5]
    #n1 = len(n)
    nai(n)
    