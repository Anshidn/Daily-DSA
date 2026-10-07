class Solution:
    def reverseWords(self, s: str) -> str:
        splited_str=s.split()
        out=""
        for i in range (len(splited_str)):
            a=str(splited_str[i][::-1])
            out+="".join(a)
            out+=" "
        return out[:-1]