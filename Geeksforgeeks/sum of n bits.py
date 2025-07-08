def find_n(s,n,prefix,res):
    if n == 0:
        res.append(prefix)
        return
    for i in range(2):
        newprefix = prefix+s[i]
        find_n(s,n-1,newprefix,res)
    return res
def sum_num(num):
    summ = 0
    for i in range(len(num)):
        summ += int(num[i])
    return summ
def find_right(n):
    s= ["0","1"]
    res = []
    find_n(s,n,"",res)
    n = len(res)
    #return res, n
    final_result = []
    for i in range(n):
        for j in range(i, n):
            if (sum_num(res[i])-sum_num(res[j])) == 0 and (res[i]+res[j]) not in final_result:
                final_result.append(res[i]+res[j])
    return final_result
if __name__ == "__main__":
    n = 3
    #t = "012"
    #print(sum_num(t))
    print(find_right(n))



