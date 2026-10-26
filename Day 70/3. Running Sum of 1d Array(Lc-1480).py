#code

class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        n=len(nums)
        ans=[0]*n
        ans[0]=nums[0]
        for i in range(1,n):
            ans[i]=nums[i]+ans[i-1]
        return ans

Link-https://leetcode.com/problems/running-sum-of-1d-array/
        
