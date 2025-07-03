def subsetg(idx, s, curr, res):
    if idx == len(s):
        res.append(list(curr))
        return
    #include in subset
    curr.append(s[idx])
    subsetg(idx+1, s, curr, res)
    #exclude from subset
    curr.pop()
    subsetg(idx+1, s, curr, res)
def subset(s):
    subset = []
    s.sort()
    res = []
    subsetg(0,s,subset,res)
    res.sort()
    return res

if __name__ == "__main__":
    st = [1,2,3]

    res = subset(st)
    for subs in res:
        for num in subs:
            print(num,end=" ")
        print()