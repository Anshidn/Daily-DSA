class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        nums1=sorted(nums1)
        nums2=sorted(nums2)
        for i in range(len(nums1)):
            x=nums2[i]-nums1[i]
            return x