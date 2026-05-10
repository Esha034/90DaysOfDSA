class Solution:
    def subarraysWithXorK(self, nums, k):
        count=0
        xr=0
        mp={0:1}
        for num in nums:
            xr^=num
            x=xr^k
            if x in mp:
                count+=mp[x]
            mp[xr]=mp.get(xr,0)+1
        return count
