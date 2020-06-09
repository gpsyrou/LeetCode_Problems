'''
1299. Replace Elements with Greatest Element on Right Side

Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

After doing so, return the array.
'''
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        final_array = []
        length_arr = len(arr)
        for i in range(length_arr):
            if i == (length_arr-1):
                final_array.append(-1)
            else:
                final_array.append(max(arr[i+1:length_arr]))
                
        return final_array
