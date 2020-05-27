'''
Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.
'''
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        final_list = []
        for num_i in nums:
            smaller_numbers_count = 0
            for j in range(0, len(nums)):
                if  num_i > nums[j]:
                    smaller_numbers_count+=1
        
            final_list.append(smaller_numbers_count)
        return final_list

