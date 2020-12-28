'''
1662. Check If Two String Arrays are Equivalent

Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.

A string is represented by an array if the array elements concatenated in order forms the string.
'''
class Solution:
    def mergeString(self, word_list: List[str]) -> str:
        return ''.join([x for x in word_list])
    
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        if self.mergeString(word1) == self.mergeString(word2):
            return True
        else:
            return False