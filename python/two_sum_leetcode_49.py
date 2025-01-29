
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} # val : index map

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:   
                return [prevMap[diff], i] 
             #as 7-3 = 4, we dont ve 4 on our hashmap so again loop for next, now 7-4=3 here we have 3 in our hashmap
             #  prevMap[3] index 0
            prevMap[n] = i ## first hash map is empty and adding the values

d = Solution()
print(d.twoSum([3,4,5,6], 7))

# Time complexity: o(n)
# Space complexity: O(n)

            