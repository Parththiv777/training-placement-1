class Solution(object):
    def isPalindrome(self, x):
        string=str(x)
        n=len(string)
        test=True
        for i in range(n // 2):
            if string[i]!=string[n-i-1]:
                return False
        return test

        
