'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
'''
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        prefix = ""
        
        if not strs: 
            return prefix
        
        s_str = min(strs, key=len)
        
        for i in range(len(s_str)):
            if all([x.startswith(s_str[:i+1]) for x in strs]):
                prefix = s_str[:i+1]
            else:
                break
                
        return prefix

