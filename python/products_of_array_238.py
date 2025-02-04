from typing import List


# 1. Brute Force Method
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        res = [0] * n

        for i in range(n):
            prod = 1
            for j in range(n):
                if i == j:
                    continue
                prod *= nums[j] 
            res[i] = prod
        return res
    

# Time Complexity: o(n2)
# Space Complexity: O(1)

d = Solution()
print(d.productExceptSelf([1,2,4,6]))