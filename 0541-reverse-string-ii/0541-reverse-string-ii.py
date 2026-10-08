class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        answer=""
        for i in range(0,len(s),k * 2):
            part=s[i:i+k]
            answer +=part[::-1]
            part=s[i+k:i+2*k]
            answer+=part
        return answer