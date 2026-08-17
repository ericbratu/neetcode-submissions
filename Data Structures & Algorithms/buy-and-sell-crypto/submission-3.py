class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0
        length = len(prices)
        sell = prices[0]
        

        for i in range(length):
            buy = prices[i]
            if buy > sell:
                profit = max(profit, buy - sell)
            else:
                sell = buy
        return profit