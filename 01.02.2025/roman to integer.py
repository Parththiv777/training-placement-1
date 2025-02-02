class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = 0
        dict = {"I": 1,"V": 5,"X": 10,"L": 50,"C": 100,"D": 500,"M": 1000 }
        i = 0
        while(i<len(s)):
            if i+1 < len(s) and dict[s[i+1]]>dict[s[i]]:
                total+= -dict[s[i]]
            else:
                total+= dict[s[i]]
            i+=1
        return total
