class Solution:
    def maxProfit(self, prices):
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            max_profit = max(max_profit, profit)

        return max_profit


#bruteforce
class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        n=len(nums)
        max_profit=0
        for i in range(n):
            for j in range(i+1,n):
                profit=0
                if nums[i]<nums[j]:
                    profit=nums[j]-nums[i]
                    max_profit=max(max_profit,profit)
        return max_profit
