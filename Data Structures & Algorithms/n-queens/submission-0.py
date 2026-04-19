class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols,pD,nD=set(),set(),set()
        res=[]
        board=[["."]*n for i in range(n)]
        def bT(r):
            if r==n:
                copy= ["".join(row) for row in board]
                res.append(copy)
                return res
            for c in range(n):
                if c in cols or (r+c) in pD or (r-c) in nD:
                    continue
                cols.add(c)
                pD.add(r+c)
                nD.add(r-c)
                board[r][c] = "Q"

                bT(r+1)
                cols.remove(c)
                pD.remove(r+c)
                nD.remove(r-c)
                board[r][c]="."
        bT(0)
        return res