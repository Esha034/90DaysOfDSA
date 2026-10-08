class Solution:
    def NthRoot(self, n, m):

        low,high=1,m

        while low<=high:
            mid=(low+high)//2
            power=1

            for i in range(n):
                power *= mid
            if power== m:
                return mid
            elif power > m:
                high=mid-1
            else:
                low=mid+1
        return -1

      
