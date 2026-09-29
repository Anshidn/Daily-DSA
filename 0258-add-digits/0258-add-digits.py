class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            listed=list(str(num))
            total=0
            for i in range(len(listed)):
                total+=int(listed[i])
            num=total
        return num