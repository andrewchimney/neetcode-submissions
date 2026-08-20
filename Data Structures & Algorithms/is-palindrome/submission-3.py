class Solution:
    def isPalindrome(self, s: str) -> bool:
        s2 = "".join(c.lower() for c in s if c.isalnum())
        for i in range(len(s2)):
            if(s2[i] != s2[-i-1]):
                return False
        return True

        