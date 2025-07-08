def isPalindrom(s):
    return s == s[::-1]  #provide true/false
def backtracking(idx, curr, res, s):              #idx: current index, curr:current list, res:final list of partition
    if idx == len(s):
        res.append(curr[:])             #curr[:] creates a copy of curr to avoid reference issues.
        return               #control back to the previous recursive call
    temp = ""
    for i in range(idx, len(s)):
        temp += s[i]
        if isPalindrom(temp):
            curr.append(temp)
            backtracking(i+1,curr,res,s)
            curr.pop()

def palindrom(s):
    res = []
    backtracking(0,[], res, s)
    return res
if __name__ == "__main__":
    s = "abcba"
    res = palindrom(s)
    for part in res:
        print(" ".join(part))