def firstvalue(s,idx):
    if ord(s[idx])<91 and ord(s[idx])>64:
        print(s[idx])
        return
    firstvalue(s,idx+1)
if __name__ == "__main__":
    s = "geeksforgeeKs"
    firstvalue(s,0)
