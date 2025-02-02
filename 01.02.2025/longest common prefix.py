class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s=''
        a=min(strs,key=len)
        for i in range(len(a)):
            b=a[i]
            if all(nm[i]==b for nm in strs):
                s+=b
            else:
                break
        return s

        
