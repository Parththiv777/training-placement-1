class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        a=len(nums)-1
        for i in range(len(nums)):
         if target==nums[i]:
            return i
        else:
           for i in range(len(nums)):
             if(nums[a]<target):
              return len(nums)
             elif nums[i]<target and nums[i+1]>target:
                return i+1
             elif nums[0]>target:
              return 0

    
        
        
