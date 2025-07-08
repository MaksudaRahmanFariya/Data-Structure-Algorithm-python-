def permutation(s, idx,res):
    if idx == len(s):
        res.append("".join(s))
        return
    for i in range(idx,len(s)):
        s[idx], s[i] = s[i],s[idx]
        permutation(s,idx+1,res)
        s[idx],s[i] = s[i],s[idx]
def find_all(s):
    res = []
    permutation(list(s),0, res)
    res.sort()
    return res
if __name__ == "__main__":
    s = "ABC"
    print(find_all(s))


