def power_set(s,n,idx=-1,curr=""):
    if idx == n:
        return
    if len(curr)>0:
        print(curr)
    for i in range(idx+1,n):
        curr+=s[i]
        power_set(s,n,i,curr)
        curr = curr[:len(curr)-1]
def show(s):
    s = ''.join(sorted(s))
    power_set(s,len(s))
if __name__ == "__main__":
    s = "cab"
    show(s)