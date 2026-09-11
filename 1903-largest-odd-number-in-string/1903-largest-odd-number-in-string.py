class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num)):
            if int(num[-1]) % 2 == 1:
                return num
            else:
                num=num[:-1]
        return ""
            