class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = prices[0]
        max_profit = 0
        curr_profit = 0
        for i in range(1,len(prices)):
            if prices[i]<mini:
                mini = prices[i]
            curr_profit = prices[i]-mini
            max_profit = max(curr_profit,max_profit)
        return max_profit