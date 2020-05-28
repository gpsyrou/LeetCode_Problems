'''
1295. Find Numbers with Even Number of Digits

Given an array nums of integers, return how many of them contain an even number of digits.
'''
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        number_of_even_nums = 0
        for val in nums:
            if len(str(val)) % 2 == 0:
                number_of_even_nums += 1
        return number_of_even_nums
