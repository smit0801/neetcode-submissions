class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea=0
        stack = []
       
        for i,n in enumerate(heights):
            start = i
            while stack and stack[-1][1]>n:
                index,height = stack.pop()
                maxArea=max(maxArea,height * (i-index))
                start = index
            stack.append((start,n))
        for i,n in stack:
            maxArea = max(maxArea, n * (len(heights)-i))
        return maxArea


        