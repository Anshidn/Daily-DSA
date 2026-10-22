class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels=["a","e","i","o","u"]
        result = ""
        vowel=0
        consonent=0
        for char in s:
            if char in vowels:
                vowel=max(vowel, s.count(char))
            else:
                consonent=max(consonent, s.count(char))
        return vowel+ consonent