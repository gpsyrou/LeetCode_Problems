'''
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.
'''

class Solution:
    
    def hammingDistance(self, x: int, y: int) -> int:
        
        binary_x = list(bin(x)[2:].zfill(31))
        binary_y = list(bin(y)[2:].zfill(31))
        
        non_common = 0
        for i in range(0,len(binary_x)):
            if binary_x[i] != binary_y[i]:
                non_common += 1
        
        return non_common

                
# Example
x = Solution()
x.hammingDistance(12,178)
