from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows= defaultdict(set)
        cols=defaultdict(set)       # here the key is the index itself
        subsq= defaultdict(set) # where key is index=(r//3,c//3) round down. boxes are assigned 0,1,3 index        
        
        for r in range(9):
            for c in range(9):
                if board[r][c]==".":
                    continue
                if (board[r][c] in rows[r] or 
                    board[r][c] in cols[c] or
                    board[r][c] in subsq[(r//3,c//3)]):

                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                subsq[(r//3,c//3)].add(board[r][c])
        return True