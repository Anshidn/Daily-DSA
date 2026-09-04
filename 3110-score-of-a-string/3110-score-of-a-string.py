class Solution:
    def scoreOfString(self, s: str) -> int:
        score=[]
        for i in range(len(s)-1):
            a=abs(ord(s[i])-ord(s[i+1]))
            score.append(a)
            
        return sum(score)    