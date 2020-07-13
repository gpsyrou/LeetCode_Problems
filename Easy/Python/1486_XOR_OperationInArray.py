'''
1486. XOR Operation in an Array

Given an integer n and an integer start.

Define an array nums where nums[i] = start + 2*i (0-indexed) and n == nums.length.

Return the bitwise XOR of all elements of nums.
'''
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        ls = [start + 2*i for i in range(n)]
        output = reduce(lambda x, y: x^y, ls)
        return output
