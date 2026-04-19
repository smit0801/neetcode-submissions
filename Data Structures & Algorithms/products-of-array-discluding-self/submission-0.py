class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        i=0
        res=[]
        for i in range(len(nums)):
            product=1
            for j in range(len(nums)):
                if j != i:
                    product *= nums[j]
            res.append(product)
        return res
