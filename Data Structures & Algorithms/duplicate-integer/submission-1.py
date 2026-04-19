class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        done=set()
        for i in nums:
            if i in done:
                return True
            else:
                done.add(i)
        return False
       
        