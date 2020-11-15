'''
Given an integer number n, return the difference between the product of its digits and the sum of its digits. 
'''
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod, sm = 1, 0
        for digit in list(str(n)):
            prod *= int(digit)
            sm += int(digit)
        return prod - sm
