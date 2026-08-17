class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        length = len(prices)

        profit = 0
        sell = prices[0]

        for i in range(length):
            if prices[i] > sell:
                profit = max(profit, prices[i] - sell)
            else:
                sell = prices[i]
        return profit
            