class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)

        profit = 0

        buy = prices[0]

        for i in range(length):
            sell = prices[i]
            if sell > buy:
                profit = max(profit, sell - buy)
            else:
                buy = sell

        return profit