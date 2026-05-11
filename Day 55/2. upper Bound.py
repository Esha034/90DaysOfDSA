class Solution:
    def upperBound(self, nums, x):
        n=len(nums)
        ind=n
        low,high=0,n-1
        while low<=high:
            mid=(low+high)//2

            if nums[mid]>x:
                ind=mid
                high=mid-1
            else:
                low=mid+1
        return ind
