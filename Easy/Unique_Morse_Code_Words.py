'''
Now, given a list of words, each word can be written as a concatenation of the Morse code of each letter. For example, "cba" can be written as "-.-..--...", (which is the concatenation "-.-." + "-..." + ".-"). We'll call such a concatenation, the transformation of a word.

Return the number of different transformations among all words we have.

Example:
Input: words = ["gin", "zen", "gig", "msg"]
Output: 2

'''
class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]     
        letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        final, dct = [], {}
        
        for i in zip(letters,morse): 
            dct[i[0]] = i[1]
            
        for word in words:
            let_list = list(word)
            temp = ''
            for j in let_list:
                temp = temp + dct[j]
             
            final.append(temp)
            
        return len(set(final))

X = Solution()
X.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"])
