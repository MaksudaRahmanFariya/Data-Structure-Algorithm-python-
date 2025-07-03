n, k = map(int,input().split())
a = list(map(int,input().split()))
unused = 0
sur = 0
for i in a:
    if i>k:
        unused +=i - k
    elif i < k:
        sur += k - i
print(unused, sur)