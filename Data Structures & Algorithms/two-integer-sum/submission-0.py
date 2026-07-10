class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_num={}
        for i in range(len(nums)):
            val=target-nums[i]
            if val in seen_num:
                return [seen_num[val],i]

            seen_num[nums[i]]=i
        