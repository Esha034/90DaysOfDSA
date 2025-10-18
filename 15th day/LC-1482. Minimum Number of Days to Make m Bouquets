class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if m * k > n:
            return -1

        # find min and max day manually
        minday = bloomDay[0]
        maxday = bloomDay[0]
        for i in range(1, n):
            if bloomDay[i] < minday:
                minday = bloomDay[i]
            if bloomDay[i] > maxday:
                maxday = bloomDay[i]

        low = minday
        high = maxday
        res = -1

        while low <= high:
            mid = (low + high) // 2

            flowers = 0
            bouquets = 0
            # count possible bouquets on day = mid
            for i in range(n):
                if bloomDay[i] <= mid:
                    flowers += 1
                    if flowers == k:
                        bouquets += 1
                        flowers = 0
                else:
                    flowers = 0

            # binary search adjustment
            if bouquets >= m:
                res = mid
                high = mid - 1   # try smaller day
            else:
                low = mid + 1    # need more days

        return res


   
        
# #bruteforce
#         n=len(bloomDay)
#         if m*k>n:
#             return -1

#         minday=bloomDay[0]
#         maxday=bloomDay[0]
#         for i in range(n):
#             if bloomDay[i]<minday:
#                 minday=bloomDay[i]
#             if bloomDay[i]>maxday:
#                 maxday=bloomDay[i]

#         for day in range(minday,maxday+1):
#             flowers=0
#             bouquets=0
#             for i in range(n):
#                 if bloomDay[i]<=day:
#                     flowers+=1
#                     if flowers==k:
#                         bouquets+=1
#                         flowers=0
#                 else:
#                     flowers=0
#             if bouquets>=m:
#                 return day



        
