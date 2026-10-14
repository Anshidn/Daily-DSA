class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        num=[]

        for i in nums:
            n=i*i
            num.append(n)
            
        num.sort()
        
        return num