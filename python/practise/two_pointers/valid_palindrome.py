# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#        reverseString = s[::-1]
#        givenString = "".join(char for char in s if char.isalnum())
#        reverseString = "".join(char for char in s if char.isalnum())
#        if givenString.lower() == reverseString.lower():
#            return True
#        return False

## 1. Reverse String Method

# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         newStr = ""
#         for c in s:
#             if c.isalnum():
#                 newStr += c.lower()
#         return newStr == newStr[::-1]
    
# Time Complexity: O(n)
#Space Complexity: O(n)


 ## 2. Two Pointer Method 

class Solution:
    def isPalindrome(self, s: str) -> bool: 
        l, r = 0, len(s) -1
      
        while l < r:
            if l < r and not self.alphaNum(s[l]):
                l += 1
            if r > 1 and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l+1, r-1
        return True
    
    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or 
                ord('a') <= ord(c) <= ord('z') or 
                ord('0') <= ord(c) <= ord('9'))


# Time Complexity: O(n)
#Space Complexity: O(1)    
        
d = Solution()
print(d.isPalindrome("Was it a car or a cat I saw?"))
