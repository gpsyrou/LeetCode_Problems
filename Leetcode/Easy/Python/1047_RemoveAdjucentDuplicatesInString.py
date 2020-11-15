'''
1047. Remove All Adjacent Duplicates In String

Given a string S of lowercase letters, a duplicate removal consists of choosing two adjacent and equal letters, and removing them.

We repeatedly make duplicate removals on S until we no longer can.

Return the final string after all such duplicate removals have been made.  It is guaranteed the answer is unique.
'''

class Solution:
    def removeDuplicates(self, S: str) -> str:
        strng = list(S)
        s = len(strng)
        while s != 0:
            for i in range(s+1):
                if (i == (len(strng)-1)):
                    s = 0
                    break
                elif strng[i] == strng[i+1]:
                    del strng[i:i+2]
                    s -= 2
                    break
                else:
                    continue
        return ''.join([x for x in strng])