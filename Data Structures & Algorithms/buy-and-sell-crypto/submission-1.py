class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        x=min(prices)
        profit=0
        for i in prices:
            if i - x > profit:
                profit= i - x
        return profit
        
    
        