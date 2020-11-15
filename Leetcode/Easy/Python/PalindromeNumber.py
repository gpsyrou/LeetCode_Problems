'''
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true

'''

class Solution:

    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        z = 0

        if len(x) == 1:
            flag = True
        else:
            for i in range(0, int(len(x)/2)-1):
                if x[i] == x[-1+z]:
                    flag = True
                    z+=1
                else:
                    flag = False
        return flag            




x = Solution()
x.isPalindrome(121)
