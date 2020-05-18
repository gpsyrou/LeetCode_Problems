'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
'''
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        ls_len = len(strs)
        strs = sorted(strs, key=len)
        for indx, letter in enumerate(strs[0]):
            equal = False
            for i in range(1, ls_len):
                try:
                    if strs[i][indx] == letter:
                        equal = True
                    else:
                        equal = False
                except IndexError:
                    pass

            if equal is True:
                prefix += letter
                
        return prefix

