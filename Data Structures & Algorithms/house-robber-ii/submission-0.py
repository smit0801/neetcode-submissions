class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        
        def robber(nums):

            robd,robc=0,0
            for n in nums:
                temp=max(n+robd,robc)
                robd=robc
                robc=temp
            return robc

        return max(robber(nums[1:]),robber(nums[:-1]))
        