class Solution(object):
    def removeDuplicates(self, nums):
        n=len(nums)
        k=0
        for i in range(n-1):
            if nums[i]!=nums[i+1]:
                nums[k+1]=nums[i+1]
                k+=1
        return k+1
