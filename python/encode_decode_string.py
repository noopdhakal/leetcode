from typing import List
class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s))+"#"+ s # output --> 4#neet4#code4#love3#you
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#": ## until we found # key we keep incrementing j + 1
                j = j + 1        
            length = int(s[i:j]) ## j not included s[i:j] return first 4 not #
            res.append(s[j+1: j+1+length])
            i = j + 1 + length
        return res

## Time Complexity: O(m) for encode and decode
## Space Complexity: o(1) for encode and decode

d = Solution()
print(d.encode(["neet","code","love","you"]))
print(d.decode("4#neet4#code4#love3#you"))