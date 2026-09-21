class Solution:
    def repeatedNTimes(self, nums: list[int]) -> int:
        n=len(nums)//2
        count={}
        for num in nums:
            if num in count:
                count[num]+=1
            else:
                count[num] = 1
        for num in count:
            if count[num] == n:
                return num
            

