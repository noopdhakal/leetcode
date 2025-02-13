
from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) -1

        while l < r:

            curSum = numbers[l] + numbers[r]

            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return [l+1, r+1] ## as we need index start from 1 not 0 so returning values
        return []


d = Solution()
print(d.twoSum([1,2,3,4], target = 3))