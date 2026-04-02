class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        l = 0

        for r in range(len(prices)):
            while r<len(prices) and prices[l]>prices[r]:
                l+=1
            current_profit = prices[r]-prices[l]
            max_profit = max(max_profit,current_profit)
        
        return max_profit

            
                


        