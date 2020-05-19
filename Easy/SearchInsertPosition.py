'''
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.
'''

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for index, number in enumerate(nums):
            # Check if the number matches the target - if yes return the index
            if number == target:
                return index
            else:
                # Check if the next number is higher
                if nums[index+1] > target:
                    return index
                elif 
