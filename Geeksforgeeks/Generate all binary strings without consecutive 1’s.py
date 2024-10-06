def generatestrunit(K,str,n):
    if n == K:
        print(*str[:n],sep = "",end=" ")
        return
    if (str[n-1] == '1'):
        str[n] = '0'
        generatestrunit(K,str,n+1)
    if str[n-1] == '0':
        str[n] = '0'
        generatestrunit(K,str,n+1)
        str[n] = '1'
        generatestrunit(K,str,n+1)
def generateall(K):
    if (K<=0):
        return
    # binary string of length K
    str = [0] * K
    str[0] = '0'
    generatestrunit(K,str,1)
    str[0] = '1'
    generatestrunit(K,str,0)
if __name__ == "__main__":
    K = 4
    generateall(K)




