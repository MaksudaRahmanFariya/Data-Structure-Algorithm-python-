def remove_consecutive(s, idx, output):
    if idx == len(s)-1:
        output+=s[idx]
        return output
    if s[idx] != s[idx+1]:
        output += s[idx]


        #return remove_consecutive(s,idx+1,output)
    return remove_consecutive(s,idx+1,output)
if __name__ == "__main__":
    s = "aaaa"
    output = ""

    print(remove_consecutive(s,0, output))

