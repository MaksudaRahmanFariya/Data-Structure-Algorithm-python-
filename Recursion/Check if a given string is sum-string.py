def add_string(num1,num2):
    if len(num1) < len(num2):
        num1,num2 = num2,num1
    len1 = len(num1)
    len2 = len(num2)
    summ = ""
    carry = 0
    # Add from least significant digits
    for i in range(len2):
        d1 = ord(num1[len1-1-i]) - ord('0') #convert character to integer
        d2 = ord(num2[len2-1-i]) - ord('0')
        digit = (d1+d2+carry) % 10
        carry = (d1+d2+carry)//10
        summ = chr(digit+ord('0'))+summ
    for i in range(len2,len1):
        d = ord(num1[len1-1-i]) - ord('0')
        digit = (d+carry) % 10
        carry = (d+carry)//10
        summ = chr(digit + ord('0')) + summ
    if carry:
        summ = chr(carry+ord('0'))+summ
    return summ
def checkSequence(s,start,len1,len2):
    part1 = s[start:start+len1]
    part2 = s[start+len1:start+len1+len2]
    if (len(part1)>1 and part1[0] == '0') or (len(part2)>1 and part2[0]=='0'):
        return False
    exsum = add_string(part1,part2)
    sumlen = len(exsum)
    if start+len1+len2+sumlen>len(s):
        return False
    part3 = s[start+len1+len2:start+len1+len2+sumlen]
    if (len(part3)>1 and part3[0] == '0'):
        return False
    if exsum == s[start+len1+len2:start+len1+len2+sumlen]:
        if start+len1+len2+sumlen == len(s):
            return True
        return checkSequence(s,start+len1,len2,sumlen)
    return False
def isSumString(s):
    n = len(s)
    for len1 in range(1,n):
        for len2 in range(1,n-len1):
            if checkSequence(s,0,len1,len2):
                return True
    return False

if __name__ == "__main__":
    s = "12243660"
    print("true" if isSumString(s) else "false")


