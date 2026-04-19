class Solution:
    def countBits(self, n: int) -> List[int]:
        output=[]
        for i in range(n+1):
            ct=0
            while i:
                i=i & (i-1)
                ct+=1
            output.append(ct)
        return output    
