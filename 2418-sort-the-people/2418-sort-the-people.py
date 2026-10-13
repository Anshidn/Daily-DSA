class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        out=[]
        for i in range(len(names)):
            out.append((heights[i],names[i]))
        
        out.sort(reverse=True)

        answer=[]
        for height,name in out:
            answer.append(name)
        return answer
            