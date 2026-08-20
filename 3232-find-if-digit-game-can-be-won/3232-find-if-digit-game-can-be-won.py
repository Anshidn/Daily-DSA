class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        single = 0
        double = 0
        for i in range(len(nums)):
            if nums[i] <10:
                single += nums[i]
                print(single)
            else:
                double += nums[i]

        if single < double:
            return True
        elif single > double:
            return True
        else:
            return False