class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevM= {}
        
        for i in range(len(nums)):
            n=nums[i]
            diff = target - n
            if diff in prevM:
                return [prevM[diff],i]
            prevM[n]= i

