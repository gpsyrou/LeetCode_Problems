'''
Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.

Example:

Input: 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.
'''

class Solution:
    """ Calculate the binary complement of a number"""
    def findComplement(self, num: int) -> int:
        binary = bin(num)[2:]
        fnl = str()
        for i in binary: 
            if i == '1':
                fnl += str(0)
            else:
                fnl += str(1)
                
        return int(fnl, 2)

x = Solution()
x.findComplement(5)
