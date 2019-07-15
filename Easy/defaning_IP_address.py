class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        return address.replace(".","[.]")
        
x = Solution()
x.defangIPaddr("1.1.0.1")
