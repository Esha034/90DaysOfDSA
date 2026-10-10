lass Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_pile=0
        n=len(piles)
        for i in range(n):
            if piles[i]>max_pile:
                max_pile=piles[i]
       
        low,high=1,max_pile
        res=high
        while low<=high:
            mid=(low+high)//2
            hours=0
            for pile in piles:
                hours+=(pile+mid-1)//mid
            if hours <=h:
                res=mid
                high=mid-1
            else:
                low=mid+1
        return res



# #bruteforce
#         max_pile=0
#         n=len(piles)
#         for i in range(n):
#             if piles[i]>max_pile:
#                 max_pile=piles[i]

#         for k in range(1,max_pile+1):
#             hours=0
#             for pile in piles:
#                 hours+=(pile+k-1)//k

#             if hours<=h:
#                 return k
#         return max_pile
        
