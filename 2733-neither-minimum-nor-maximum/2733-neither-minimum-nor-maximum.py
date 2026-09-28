class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        my_set = set(nums)
        print(my_set)
        if len(my_set) > 2:
            nums=sorted(nums)
            return nums[1]
            print(nums)
        else:
            return -1

            