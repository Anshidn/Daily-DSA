class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel=0

        for i in range(len(stones)):
            if stones[i] in jewels:
                jewel+=1

        return jewel