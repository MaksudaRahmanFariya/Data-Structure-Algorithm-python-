def final_sol(res):
    if not res:
        print("[]")
    else:
        print(" ".join(res))

def permutation(num,res,target,expression,idx,evalval,last):
    if idx == len(num):
        if evalval == target:
            res.append(expression)
        return



if __name__ == "__main__":
    num = "123"
    operation = ["*","-","+"]
    for i in range(2):
        num += num[:i+1] + operation[i] + num[i+1:-1]
    print(num)