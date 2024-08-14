import math as mt
def ternary_search(l,r,key,ar):
    if (r >= l) :
        mid1 = l+(r-l)//3
        mid2 = r - (r-l)//3
        if(ar[mid1]==key):
            return mid1
        elif (ar[mid2]==key):
            return mid2
        elif(ar[mid1]>key):
            return ternary_search(l,mid1-1,key,ar)
        elif(ar[mid2]>key):
            return ternary_search(mid1+1,mid2-1,key,ar)
        else:
            return ternary_search(mid2+1,r,key,ar)
    return -1
if __name__ == "__main__":
    l, r, key = 0, 9, 5
    ar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    p = ternary_search(l, r, key, ar)
    print("Index of", key, "is", p)



