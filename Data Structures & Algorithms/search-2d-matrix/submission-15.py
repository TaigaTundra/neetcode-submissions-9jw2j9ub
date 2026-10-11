class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        l,r = 0, (rows*cols)-1 

        while l<=r:
            m = (l+r) //2 
            entry_m = matrix[m//cols][m%cols]
            if entry_m > target:
                r = m-1
            elif entry_m < target:
                l = m+1
            else:
                return True 
        
        return False 

