class Solution:
    def isPalindrome(self, s: str) -> bool:
        s2=s
        s= ""
        for c in s2:
            if c.isalnum():
                s+=c.lower()
        for i in range(len(s)):
            print(s[i]," ",s[-i-1])
            if(s[i] != s[-i-1]):
                return False
        return True

        