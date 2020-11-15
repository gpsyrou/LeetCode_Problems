'''
961. N-Repeated Element in Size 2N Array

In a array A of size 2N, there are N+1 unique elements, and exactly one of these elements is repeated N times.

Return the element repeated N times.
'''
class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        d= {}
        for num in A:
            if num not in d.keys():
                d[num] = 0
            else:
                d[num] += 1
        return max(d, key = d.get)
