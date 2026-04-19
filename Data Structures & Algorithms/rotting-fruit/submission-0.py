class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid),len(grid[0])
        q=deque()
        good=0
        def bfs(r,c):
            nonlocal good
            if (r<0 or c<0 or c>=cols or r>=rows  or grid[r][c]!=1):
                return
            grid[r][c]=2
            good-=1
            q.append([r,c])
            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    good+=1
                if grid[r][c]==2:
                    q.append([r,c])
                    
                    
        time=0
        while q and good>0:
            for i in range(len(q)):
                r,c=q.popleft()
                bfs(r-1,c)
                bfs(r,c-1)
                bfs(r,c+1)
                bfs(r+1,c)
            time+=1 
        return time if  good==0 else -1


            
        