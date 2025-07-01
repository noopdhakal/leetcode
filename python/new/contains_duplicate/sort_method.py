from typing import List
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False


d = Solution()
print(d.hasDuplicate([1, 2, 3, 3]))
print(d.hasDuplicate([1, 2, 3, 4]))

# Time Complexity: o(nlogn)
# Space Complexity: O(1)