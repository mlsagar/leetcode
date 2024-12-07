class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        min_price = float("inf")

        for i in range(len(prices)):
            if min_price > prices[i]:
                min_price = prices[i]
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i]
        return max_profit