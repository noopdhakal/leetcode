from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}

        for i, n in enumerate(nums):

            diff = target - n

            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i ## update hashmap
        return 



d = Solution()
print(d.twoSum([3,4,5,6], 7))
print(d.twoSum([4,5,6], 10))

# Time complexity: o(n)
# Space complexity: O(n)