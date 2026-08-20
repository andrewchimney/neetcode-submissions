class Solution:
    def isValid(self, s: str) -> bool:
        li=[]
        for i in range(len(s)):
            if(s[i]=='(' or s[i]=='{' or s[i]=='['):
                li.append(s[i])
            else:
                if(not li):
                    return False
                match=li.pop()
                if(match=='(' and s[i]!=')'):
                    return False
                if(match=='{' and s[i]!='}'):
                    return False
                if(match=='[' and s[i]!=']'):
                    return False
        if(li):
            return False
        return True
        