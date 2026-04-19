class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:                       # problem statement me n>1 so useless
            return True
        preMap= {i:[] for i in range(n)}
        for a,b in edges:
            preMap[a].append(b)                 # 2 cause undirected
            preMap[b].append(a)
        visit= set()
        def dfs(i,prev):
            if i in visit:
                return False
            
            visit.add(i)
            for j in preMap[i]:
                if j == prev:
                    continue
                if not dfs(j,i):
                    return False
            return True

        return dfs(0,-1) and len(visit)==n