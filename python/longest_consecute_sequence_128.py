from typing import List

# 1. Brute force method
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        store = set(nums)
        
        for num in nums:
            streak, curr = 0, num
            while curr in store:
                # print(curr)
                streak += 1
                curr += 1
            res = max(res, streak)
        return res

d = Solution()
print(d.longestConsecutive([0,3,2,5,4,6,1,1]))
