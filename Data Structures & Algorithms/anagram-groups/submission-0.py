class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sigs = {}
        for s in strs:
            signature = [0] * 26
            for c in s:
                signature[ord(c)-97]+=1
            signature = tuple(signature)    
            if signature in sigs:
                sigs[signature].append(s)
            else:
                sigs[signature] = [s]
        return list(sigs.values())