from typing import List
import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = collections.defaultdict(list)
        for s in strs:
            sortedS  = ''.join(sorted(s))
            res[sortedS].append(s)
#             res = {
#   'aet': ['eat', 'tea', 'ate'],
#   'ant': ['tan', 'nat'],
#   'abt': ['bat']88
# }
        return list(res.values())
            
            
                       
d = Solution()
print(d.groupAnagrams(["act","pots","tops","cat","stop","hat"]))

## Time Complexity: O(m*n)
## Sapce complexity: O(m)