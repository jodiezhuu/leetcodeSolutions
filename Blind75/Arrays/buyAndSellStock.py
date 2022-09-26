# You are given an array `prices` where `prices[i]` is the 
# price of a given stock on the `ith` day.

# You want to maximize your profit by choosing a **single day** 
# to buy one stock and choosing a **different day in the future** to sell that stock.

# Return *the maximum profit you can achieve from this transaction*. If you cannot 
# achieve any profit, return `0`.

# Time Complexity: O(n)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ## sliding window method
        curr_maxProfit = 0
        index = 0
        key = index + 1
        length = len(prices)
        while (key < length):
            if (prices[key] < prices[index]):
                index = key
                key += 1
            else:
                if (prices[key] - prices[index] > curr_maxProfit):
                    curr_maxProfit = prices[key] - prices[index]
                else: 
                    key += 1
        return curr_maxProfit