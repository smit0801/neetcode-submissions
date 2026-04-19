from math import sqrt
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distp=[]
        for i in range(len(points)):
            dist= sqrt((points[i][0] )**2 + (points[i][1])**2)
            distp.append([-dist,points[i][0],points[i][1]])
        heapq.heapify(distp)
        while len(distp)>k:
            heapq.heappop(distp)
        res=[]
        while  distp:
            dist,x,y= heapq.heappop(distp)
            res.append([x,y])
        return res



