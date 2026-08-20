class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ret = 0
        chars = ""
        for i in range(len(s)):
            # print(s[i])
            while(s[i] in chars):
                ret = max(len(chars), ret)
                chars = chars[1:]
        
            chars+=s[i]
        ret = max(len(chars), ret)
        return ret