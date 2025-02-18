
from typing import List

##  Two Pointer method
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums)-1
        while l < r:

            curSum = nums[l] + nums[r]

            if curSum > target:
                r-=1
            elif curSum < target:
                l+=1
            else:
                return [l+1, r+1]
        return []   


d = Solution()
print(d.twoSum([3,4,5,6], 7))

# Time complexity: o(n)
# Space complexity: O(n)