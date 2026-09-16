class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        middle=len(nums)//2
        print(middle)
        count=nums.count(nums[middle])
        print(count)
        if count == 1:
            return True 
        else:
            return False