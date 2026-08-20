class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ret = 0
        window = 0
        ha = {}
        left= 0
        right=0
        while(right<len(s)):
            ha[s[right]] = ha.get(s[right],0)+1
            window+=1
            v=max(ha.values())
            # print("highest repeated: ", v)
            # print("window: ", window)
            if(window>k+v):
                # print("window too large")
                ha[s[left]] = ha.get(s[left],0)-1
                left+=1
                window-=1
            v=max(ha.values())
            ret=max(ret, v)
            right+=1
        # print(ha)
        return min(ret+k, len(s))