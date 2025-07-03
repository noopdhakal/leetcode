from typing import List
import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c)-ord('a')] += 1
            res[tuple(count)].append(s)
            # print(res[tuple(count)])
        return list(res.values())
            
            
                       
d = Solution()
print(d.groupAnagrams(["act","pots","tops","cat","stop","hat"]))

## Time Complexity: O(m*n)
## Sapce complexity: O(m)