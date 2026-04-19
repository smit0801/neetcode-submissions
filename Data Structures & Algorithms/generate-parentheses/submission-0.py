class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        subres=[]
        def bT(o,c):
            if o==c==n:
                res.append("".join(subres))
                return
            if o<n:
                subres.append("(")
                bT(o+1,c)
                subres.pop()
            if c<o:
                subres.append(")")
                bT(o,c+1)
                subres.pop()
        bT(0,0)
        return res