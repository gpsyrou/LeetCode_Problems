'''
1684. Count the Number of Consistent Strings

You are given a string allowed consisting of distinct characters and an array of strings words. A string is consistent if all characters in the string appear in the string allowed.

Return the number of consistent strings in the array words.
'''
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        letters = [x for x in allowed]
        num_consistent = 0
        for word in words:
            is_consistent = True
            y = [x for x in word]
            for i in y:
                if i not in letters:
                    is_consistent = False
                    break
            if is_consistent == True:
                num_consistent += 1
        return num_consistent
