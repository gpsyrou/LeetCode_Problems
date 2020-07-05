'''
1207. Unique Number of Occurrences

Given an array of integers arr, write a function that returns true if and only if the number of occurrences of each value in the array is unique.
'''
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = {}
        for num in arr:
            if num not in d.keys():
                d[num] = 1
            else:
                d[num] += 1
                
        k = True
        ls = list(d.values())
        for val in ls:
            if ls.count(val) > 1:
                k = False
                break
            else:
                continue
        return k
