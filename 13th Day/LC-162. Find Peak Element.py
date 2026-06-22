class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        n = len(nums)
        l, h = 0, n - 1
        
        while l < h:
            mid = l + (h - l) // 2
            
        
            if nums[mid] < nums[mid + 1]:
                l = mid + 1
        
            else:
                h = mid
                
        return l
        
 


#brutrforce
        
        n=len(nums)
        for i in range(n):
            if nums[i]>nums[i-1] and nums[i]>nums[i+1]:
                return i
        
