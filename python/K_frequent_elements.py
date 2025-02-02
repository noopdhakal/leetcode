from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        for i in range(len(nums)):
             hashMap[nums[i]] = 1 + hashMap.get(nums[i], 0)
        res = sorted(hashMap, key = hashMap.get, reverse=True)[:2]
        return res

d = Solution()
print(d.topKFrequent([1,2,2,3,3,3], 2))
print(d.topKFrequent([7,7], 1))