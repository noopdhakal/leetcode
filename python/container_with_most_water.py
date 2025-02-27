from typing import List


## Brute Force method
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        res = 0
        
        for l in range(len(heights)):
            for r in range(l+1, len(heights)): # atleast 1 postion head of left
                area = (r-l) * min(heights[l], heights[r])
                res = max(res, area)

        return res
    


    ## Time Complexity: (on2)
    ## Space Complexity: O(1)

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        res = 0

        while l < r:
            area = min(heights[l], heights[r]) * (r - l) ## width times height, finding height of minimum
            res = max(res, area)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return res
# o(n)
# O(1)

d = Solution()
print(d.maxArea([-1,0,1,2,-1,-4]))