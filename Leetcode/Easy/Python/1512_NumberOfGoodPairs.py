'''
1512. Number of Good Pairs

Given an array of integers nums.

A pair (i,j) is called good if nums[i] == nums[j] and i < j.

Return the number of good pairs.
'''
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        good_pairs = 0
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if (i < j) and (nums[i] == nums[j]):
                    good_pairs += 1
                    
        return good_pairs
