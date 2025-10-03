class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        stockBuy = prices[0]
        profit = 0
        for price in prices[1:]:
            temp = price - stockBuy
            profit = max(profit, temp)
            stockBuy = min(price, stockBuy)
        return profit

        