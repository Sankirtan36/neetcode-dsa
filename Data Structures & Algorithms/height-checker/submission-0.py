class Solution:
    
    def heightChecker(self, heights: List[int]) -> int:
        expected=heights[:]
        self.sort(expected)
        n=len(heights)
        notEqual=0
        for i in range(n):
            if(heights[i]!=expected[i]):
                notEqual+=1
        return notEqual

    def sort(self,heights):
        n=len(heights)
        for i in range(n):
            min=i
            for j in range(i+1,n):
                if(heights[min]>heights[j]):
                    min=j
            heights[min],heights[i]=heights[i],heights[min]
        