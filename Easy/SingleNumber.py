'''
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Example 1:

Input: [2,2,1]
Output: 1

'''

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)
        if len(nums) > 1:
            for idx, number in enumerate(nums):
                if idx == 0:
                    if number < nums[1]:
                        goal = number
                        break
                if (idx > 0) and (idx < len(nums) - 2):
                    if (number == nums[idx-1]) or (number == nums[idx+1]):
                        pass
                    else:
                        goal = number
                        break
                else:  
                    goal = number     
        else:
            goal = nums[0]
        return goal

x = Solution()
x.singleNumber([4,2,1,1,2])
