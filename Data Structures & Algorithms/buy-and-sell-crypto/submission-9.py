class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        length = len(prices)

        for i in range(length - 1):
            for j in range(i + 1, length):
                if prices[i] < prices[j]:
                    currProf = prices[j] - prices[i]
                    profit = max(currProf, profit)
        return profit