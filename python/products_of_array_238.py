from typing import List


# 1. Brute Force Method
# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         n = len(nums)

#         res = [0] * n

#         for i in range(n):
#             prod = 1
#             for j in range(n):
#                 if i == j:
#                     continue
#                 prod *= nums[j] 
#             res[i] = prod
#         return res
    
# Time Complexity: o(n2)
# Space Complexity: O(1)

# 2. Division Method

# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         prod = 1
#         for num in nums:
#             prod *= num
#         res = [0] * len(nums)
#         for i, c in enumerate(nums):
#             res[i] = prod // c
#         return res
      

# Time Complexity: o(n)
# Space Complexity: O(1)

# 3. Prefix and Suffix Method

# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         n = len(nums)
#         res = [0] * n 
#         pref = [0] * n 
#         suff = [0] * n

#         pref[0] = suff[n-1] = 1 ## Prefix first 1 and suffix last 1
#         for i in range(1, n):
#             pref[i] = nums[i - 1] * pref[i-1] 
#             ## 1. nums[i-1] = nums[1-1] = nums[0] = 1, pref[1-1] = pref[0] = 1, 1*1 = 1
#             ## 2. nums[i-1] = nums[2-1] = nums[1] = 2, pref[2-1] = pref[1] = 1, 2*1 = 2
#             ## 2. nums[i-1] = nums[3-1] = nums[2] = 4, pref[3-1] = pref[2] = 2, 4*2 = 8
#         for i in range(n-2, -1, -1):
#             # i = 2, 1, 0
#             suff[i] = nums[i + 1] * suff[i+1] 
#         for i in range(n):
#             res[i] = pref[i] * suff[i]
#         return res

# Time Complexity: o(n)
# Space Complexity: O(n)

# 3. Prefix and Suffix Method (Optimal Solution)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) -1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res

# Time Complexity: o(n)
# Space Complexity: O(1)


d = Solution()
print(d.productExceptSelf([1,2,4,6]))