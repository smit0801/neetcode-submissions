class Solution:

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row,col= len(matrix) , len(matrix[0])
        def bS(row):
            l,r= 0,len(row)-1
            while l<=r:
                mid = (l+r)//2
                if row[mid]== target:
                    return True
                elif row[mid]<target:
                    l=mid+1
                else :
                    r=mid-1
            return False
        for row in matrix:
            if row[0]<= target<= row[-1]:
                if bS(row):
                    return True
        return False



        