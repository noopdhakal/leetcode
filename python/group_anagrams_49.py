from typing import List
import collections

### Sort method
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = collections.defaultdict(list)
        
        for s in strs:
            sortedS = "".join(sorted(s))
            res[sortedS].append(s)
            ## loop 1st --> act, simlarly res["act"].append("cat")
        return list(res.values())
        # return res
                
d = Solution()
print(d.groupAnagrams(["act","pots","tops","cat","stop","hat"]))