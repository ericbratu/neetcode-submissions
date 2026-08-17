class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        length = len(prices)

        buy = prices[0]

        profit = 0

        for i in range(length):
            sell = prices[i]
            if sell > buy:
                profit = max(profit, sell - buy)
            else:
                buy = sell
        return profit