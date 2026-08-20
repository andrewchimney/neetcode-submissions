class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = {}
        count_2 = {}
        for i in range(len(s)):
            if s[i] not in count:
                count[s[i]]=1
            else:
                count[s[i]]+=1
        
        for i in range(len(t)):
            if t[i] not in count_2:
                count_2[t[i]]=1
            else:
                count_2[t[i]]+=1
        
        if count==count_2:
            return True
        return False