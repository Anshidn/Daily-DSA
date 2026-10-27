class Solution:
    def smallestRangeI(self, nums: list[int], k: int) -> int:
        min_value=min(nums)
        max_value=max(nums)
        min_value+=k
        max_value-=k
        range_value=max_value - min_value
        if range_value <=0:
            return 0
        else:
            return range_value