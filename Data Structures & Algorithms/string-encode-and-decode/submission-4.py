class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for st in strs:
            encoded_str += str(len(st))
            encoded_str += ":"
            encoded_str += st
        # print("encoded: ", encoded_str)
        return encoded_str

    def decode(self, s: str) -> List[str]:
        li = []
        length = ""
        parse = False
        i=0
        while i < len(s):
            # print("i: ",i)
            # print("length: ",length)
            # print("li ", li)

            if parse:
                st = ""
                for j in range(length):
                    st+=s[i+j]
                i+=length-1
                length = ""
                parse= False
                li.append(st)
            elif(s[i]=="0" and length==""):
                li.append("")
                i+=1
            elif(s[i]!= ":"):
                length += s[i]
            else:
                length = int(length)
                parse= True

            i+=1
        return li
