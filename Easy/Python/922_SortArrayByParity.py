'''
922. Sort Array By Parity II

Given an array A of non-negative integers, half of the integers in A are odd, and half of the integers are even.

Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.

You may return any answer array that satisfies this condition.

'''
class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        odd  = sorted([x for x in A if x%2 != 0])
        even = sorted([x for x in A if x%2 == 0])
        
        ls = []
        for i in range(len(A)):
            if i%2==0:
                ls.append(even[0])
                even.pop(0)
            else:
                ls.append(odd[0])
                odd.pop(0)
        return ls
