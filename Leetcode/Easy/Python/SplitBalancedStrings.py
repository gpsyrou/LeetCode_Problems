'''
1221. Split a String in Balanced Strings

Balanced strings are those who have equal quantity of 'L' and 'R' characters.

Given a balanced string s split it in the maximum amount of balanced strings.

Return the maximum amount of splitted balanced strings.
'''
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        balance, total = 0, 0
        for i in s:
            if i == 'L':
                balance += 1
            else:
                balance -= 1
            
            if balance == 0:
                total += 1
                
        return total
