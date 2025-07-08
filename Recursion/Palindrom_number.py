def printallKlength(s, k):
    n = len(s)
    printall(s,"",n,k)
def printall(s, prefix, n, k):
    if (k==0):
        print(prefix)
        return

    for i in range(n):
        newpre = prefix + s[i]
        printall(s,newpre, n,k-1)
if __name__ == "__main__":
    print("First Test")
    s = ["a", "b"]
    k = 3
    printallKlength(s,k)



