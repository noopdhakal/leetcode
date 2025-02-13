from typing import List



# 1. Brute Force Method
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:

#         res = set()
#         nums.sort()
#         prevMap = {}
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 for k in range(j+1, len(nums)):
#                     if nums[i] + nums[j] + nums[k] ==0:
#                         tmp = [nums[i], nums[j], nums[k]]
#                         res.add(tuple(tmp))
#                         print(res)

# Time Complexity: O(n3)
# Sapce Complexity: O(m)

## Two Pointer Method

import collections

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if a > 0:
                break
            if i > 0 and a == nums[i-1]: ## same values don't want to reuse same value twice
                continue

            l, r = i+1, len(nums) - 1 ## l = i+1 

            while l < r:
                threesum = a + nums[l] + nums[r]
                if threesum > 0:
                    r -= 1 ## decreasing sum
                elif threesum < 0:
                    l +=1 
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1 ## we don't want to use same sum
                    r-= 1
                    while nums[l] == nums[l-1] and l<r:
                        l+= 1 ## keep shifting pointer
        return res 

# Time complexity: o(n)
# space complexity: o(1) or O(n)

d = Solution()
print(d.threeSum([-1,0,1,2,-1,-4]))