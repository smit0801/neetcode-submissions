class Solution:
    def rob(self, nums: List[int]) -> int:

        robd,robc=0,0
        for n in nums:
            temp=max(n+robd,robc)
            robd=robc
            robc=temp
        return robc