from typing import List



# 1. Brute Force Method
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = set()
        nums.sort()
        prevMap = {}
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] + nums[k] ==0:
                        tmp = [nums[i], nums[j], nums[k]]
                        res.add(tuple(tmp))
                        print(res)

# Time Complexity: O(n3)
# Sapce Complexity: O(m)



d = Solution()
print(d.threeSum([-1,0,1,2,-1,-4]))