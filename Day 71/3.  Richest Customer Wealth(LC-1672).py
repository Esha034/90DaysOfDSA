#code

class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        
        maxwealth=0
        for customer in accounts:
            wealth=0
            for money in customer:
                wealth+=money
            maxwealth=max(wealth,maxwealth)
        return maxwealth
