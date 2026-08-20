class Solution:
    def isPalindrome(self, s: str) -> bool:
        s2= ""
        for c in s:
            if c.isalnum():
                s2+=c.lower()
        for i in range(len(s2)):
            if(s2[i] != s2[-i-1]):
                return False
        return True

        