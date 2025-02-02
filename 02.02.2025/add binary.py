class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        h1=int(a,2)
        h2=int(b,2)
        s=format(h1+h2,'b')
        return s
