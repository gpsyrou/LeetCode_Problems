'''
1351. Count Negative Numbers in a Sorted Matrix

Given a m * n matrix grid which is sorted in non-increasing order both row-wise and column-wise. 

Return the number of negative numbers in grid.


'''
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        sm = 0
        for outer in grid:
            for inner in outer:
                if inner < 0:
                    sm+=1
        return sm
