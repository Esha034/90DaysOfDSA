class Solution:
    def floorSqrt(self, n: int) -> int:

        if n==0 or n==1:
            return n

        low,high=1,n
        ans=0
        
        while low<=high:
            mid=low+(high-low)//2
            if mid*mid==n:
                return mid
            elif mid*mid>n:
                high=mid-1
            else:
                ans=mid
                low=mid+1
        return ans
