class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans=[]
        n=len(nums)
        i=0
        while (i<2*n):
            if (i>=n):
                ans.append(nums[i-n])

            else: 
                ans.append(nums[i])
            i+=1

        return ans