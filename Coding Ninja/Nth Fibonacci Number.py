from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.
def fibonacci(n):
    temp1,temp2 = 1,1
    if n==1 or n == 2:
        return temp1
    elif n>2:
        while n>2:
            n1= temp1
            n2 = temp2
            n3 = temp1+temp2
            n -= 1
            temp1 = temp2
            temp2 = n3
        return n3
if __name__ == '__main__':
    n = int(input())
    print(fibonacci(n))