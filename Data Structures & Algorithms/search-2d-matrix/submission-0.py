class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top,bottom=0,len(matrix)-1
        while top<=bottom:
            middle=(top+bottom)//2
            if matrix[middle][0]<=target and matrix[middle][-1]>=target:
                break
            elif matrix[middle][0]>target:
                bottom=middle-1
            elif matrix[middle][-1]<target:
                top=middle+1
        l,r=0,len(matrix[0])-1
        while l<=r:
            m=(l+r)//2
            if matrix[middle][m]==target:
                return True
            elif matrix[middle][m]>target:
                r=m-1
            else:
                l=m+1
        return False
            
         