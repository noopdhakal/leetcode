from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

d = Solution()
print(d.twoSum([3,4,5,6], 7))

# Time complexity: o(n2)
# Space complexity: O(n)