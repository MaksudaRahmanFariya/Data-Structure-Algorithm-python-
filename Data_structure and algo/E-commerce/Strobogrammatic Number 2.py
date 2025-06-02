class Solution:
    def findnum(self, n):
        final_n = n
        pairs = [('0','0'), ('1','1'), ('6','9'), ('8','8'), ('9','6')]
        def buildnum(num):
            if not num:
                return []
            if num == 1:
                return ['0', '1', '8']
            prev_result = buildnum(num-2)
            res = []
            for i in prev_result:
                for p in pairs:
                    if p[0] != 0 or num != final_n:
                        res.append(p[a]+i+p[1])
                if num != n:
                    res.append('0'+i+'0')
            return res
        return buildnum(n)
if __name__ == '__main__':
    print('Enter number: ')
    n = int(input())
    #n = 3
    p = Solution()
    print(p.findnum(n))


