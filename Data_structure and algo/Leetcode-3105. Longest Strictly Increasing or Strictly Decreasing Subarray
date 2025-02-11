class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        inc_length = dec_length = max_length = 1

        for i in range(len(nums) - 1):
            if nums[i + 1] > nums[i]:
                inc_length += 1
                dec_length = 1
            elif nums[i + 1] < nums[i]:
                dec_length += 1
                inc_length = 1
            else:
                inc_length = dec_length = 1
            
            max_length = max(max_length, inc_length, dec_length)
        
        return max_length

