from typing import List

class Solution:
    def reverse(self,St):
        #code here
        n = len(St)
        tp = []
        for _ in range(n):
            tp.append(St.pop())
        for i in range(n):
            St.append(tp[i])