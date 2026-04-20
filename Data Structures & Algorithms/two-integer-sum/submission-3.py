class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = set()
        for i in range(len(nums)):
            dif= target - nums[i]
            if dif in seen:
                return [nums.index(dif), i]
            seen.add(nums[i])