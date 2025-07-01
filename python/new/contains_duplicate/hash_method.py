from typing import List
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False


d = Solution()
print(d.hasDuplicate([1, 2, 3, 3]))
print(d.hasDuplicate([1, 2, 3, 4]))

# Time Complexity: o(n)
# Space Complexity: O(n)