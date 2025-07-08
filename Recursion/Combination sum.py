class Solution:
    def combinationsum(self, num, target):
        res = []

        def dfs(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            if i >= len(num) or total>target:
                return
            curr.append(num[i])
            dfs(i, curr, total+num[i])
            curr.pop()
            dfs(i+1, curr, total)
        dfs(0,[], 0)
        return res
num = [2,3,6,7]
target = 7
ob = Solution()
print(ob.combinationsum(num, target))

