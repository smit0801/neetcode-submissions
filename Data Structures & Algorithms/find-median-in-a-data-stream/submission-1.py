class MedianFinder:

    def __init__(self):
        self.low,self.high=[],[]


    def addNum(self, num: int) -> None:
        heapq.heappush(self.low,-num)
        if self.low and self.high and (-(self.low[0])>self.high[0]):
            n= -heapq.heappop(self.low)
            heapq.heappush(self.high,n)
        if len(self.low)> len(self.high) + 1:
            n= -heapq.heappop(self.low)
            heapq.heappush(self.high,n)
        if len(self.high)> len(self.low) + 1:
            n= heapq.heappop(self.high)
            heapq.heappush(self.low,-n)


    def findMedian(self) -> float:
        if len(self.low)>len(self.high):
            return -self.low[0]
        if len(self.low)<len(self.high):
            return self.high[0]
        return (-self.low[0]+self.high[0])/2
        