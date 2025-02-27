from typing import List

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        res = 0

        while l < r: 
            area = min(heights[l], heights[r]) * (r-l)
            res = max(res, area)
            if heights[l] <= heights[r]:
                l +=1
            else:
                r -= 1
        return res

d = Solution()
print(d.maxArea([1,7,2,5,4,7,3,6]))