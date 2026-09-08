class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        max_value=0

        for i in range(len(strs)):
            if strs[i].isdigit():
                if int(strs[i]) > max_value:
                    max_value = int(strs[i])
            else:
                if len(strs[i]) > max_value:
                    max_value = len(strs[i])
        return max_value
                
        
         