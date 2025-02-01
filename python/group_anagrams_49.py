from typing import List
import collections

# ### Sort method
# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         res = collections.defaultdict(list)
        
#         for s in strs:
#             sortedS = "".join(sorted(s))
#             res[sortedS].append(s)
#             ## loop 1st --> act, simlarly res["act"].append("cat")
#         return list(res.values())
#         # return res

## Time complexity: o(m*nlogn)
## Space complexity: O(m*n)


## Using Hash Table Method

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = collections.defaultdict(list)
        
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            # print(count) # count matches with act and cat and ate so putting values accordingly
            # print(res[tuple(count)])
            res[tuple(count)].append(s)  ## keys: 1e, 1a, 1t  values[eat, tea, ate] using keys for values
        return list(res.values())                
d = Solution()
print(d.groupAnagrams(["act","pots","tops","cat","stop","hat"]))

## Time Complexity: O(m*n)
## Sapce complexity: O(m)