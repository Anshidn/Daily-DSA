class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        answer=[]
        for i in range(len(nums)):
            left = sum(nums[:i])
            right = sum(nums[i+1:])
            difference=abs(left - right)
            answer.append(difference)
        return answer