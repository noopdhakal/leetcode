from typing import List
import collections

# 1. Brute force method
# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         res = 0
#         store = set(nums)
        
#         for num in nums:
#             streak, curr = 0, num
#             while curr in store:
#                 # print(curr)
#                 streak += 1
#                 curr += 1
#             res = max(res, streak)
#         return res

# 2. Hash set
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for num in numSet:
            if (num - 1) not in numSet:
                length =1 
                while (num + length) in numSet:
                    length += 1
                longest = max(length, longest)
            return longest
        
## Time Complexity: O(n)
## Space Complexity: O(n)


# # 3. Hash Map

# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         mp = collections.defaultdict(int)
#         res = 0
#         # print(mp)
#         for num in nums:
#             if not mp[num]:
#                 mp[num] = mp[num-1] + mp[num+1] + 1
#                 print(mp)


d = Solution()
print(d.longestConsecutive([0,3,2,5,4,6,1,1]))
