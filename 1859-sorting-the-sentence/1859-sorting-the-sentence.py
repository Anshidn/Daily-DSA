class Solution:
    def sortSentence(self, s: str) -> str:
        sentence=[""]* len(s.split())
        words=s.split()
        for word in words:
            position = int(word[-1])
            actual_word = word[:-1]

            sentence[position - 1] = actual_word

        return " ".join(sentence)