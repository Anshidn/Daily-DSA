class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        listed_string=s.split()
        out=listed_string[0:k]
        result = (" ").join(out) 
        return result    