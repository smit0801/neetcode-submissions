class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count,res= 0, nums[0]
        for i in range(len(nums)):
            if count== 0:
                res= nums[i]
                count+=1
            elif nums[i]==res:
                count+=1
            else:
                count-=1
        return res