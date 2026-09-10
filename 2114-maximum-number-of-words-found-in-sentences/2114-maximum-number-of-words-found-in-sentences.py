class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_value=0
        
        for i in range(len(sentences)):
            word=sentences[i].split()
            
            if len(word) > max_value:
                max_value = len(word)
        return max_value