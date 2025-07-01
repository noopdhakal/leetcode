from typing import List
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)


d = Solution()
print(d.hasDuplicate([1, 2, 3, 3]))
print(d.hasDuplicate([1, 2, 3, 4]))

# Time Complexity: o(n)
# Space Complexity: O(n)