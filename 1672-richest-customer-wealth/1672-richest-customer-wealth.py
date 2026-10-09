class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        large=[]
        for i in range(len(accounts)):
            total=sum(accounts[i])
            large.append(total)
        return max(large)