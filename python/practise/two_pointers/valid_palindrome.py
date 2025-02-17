class Solution:
    def isPalindrome(self, s: str) -> bool:
       reverseString = s[::-1]
       givenString = "".join(char for char in s if char.isalnum())
       reverseString = "".join(char for char in s if char.isalnum())
       if givenString.lower() == reverseString.lower():
           return True
       return False

d = Solution()
print(d.isPalindrome("Was it a car or a cat I saw?"))
