'''
977. Squares of a Sorted Array

Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.
'''
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        return sorted([x**2 for x in A])
