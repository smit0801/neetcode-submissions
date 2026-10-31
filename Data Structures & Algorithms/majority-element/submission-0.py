class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m= len(nums)//2 + 1
        freq={}
        for num in nums:
            freq[num]= freq.get(num,0) + 1

            if freq[num] >= m:
                return num
