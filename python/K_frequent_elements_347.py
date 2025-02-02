from typing import List

# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         hashMap = {}
#         for i in range(len(nums)):
#              hashMap[nums[i]] = 1 + hashMap.get(nums[i], 0)
#         res = sorted(hashMap, key = hashMap.get, reverse=True)[:2]
#         return res


## Bucket Sort Method

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums)+1)] ## Upto number of arrays
        for num in nums: ## getting hashmap with keys and values
            count[num] = 1 + count.get(num, 0)
    
        for num, cnt in count.items():    ## Adding count i , values according to the count        
            freq[cnt].append(num)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k: ## when we're going to stop when length of result matching with k
                    return res
                
### Time Complexity: o(n)
### Space Complexity: o(n)

d = Solution()
print(d.topKFrequent([1,2,2,3,3,3], 2))
print(d.topKFrequent([7,7], 1))


