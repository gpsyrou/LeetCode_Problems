class Solution(object):
    def twoSum(self, nums, target):

        ls = []
        
        for index,i in enumerate(nums): 
            zet = 1
            for itr in range(index+zet,len(nums)):
                if (nums[index] + nums[itr] == target):
                    ls.append(index)
                    ls.append(itr)
                    break
                else:
                    zet += 1      
        return ls
