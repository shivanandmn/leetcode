#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")
        max_profit = 0
        for pr in prices:
            if pr<min_price:
                min_price = pr
            else:
                # print(max_profit, min_price)
                profit = pr-min_price
                if profit>max_profit:
                    max_profit = profit
        
        return max_profit


        
# @lc code=end

