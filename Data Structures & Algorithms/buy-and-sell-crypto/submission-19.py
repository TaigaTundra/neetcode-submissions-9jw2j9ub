class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,0 
        max_profit = 0

        while r < len(prices)-1:
            if prices[l]<=prices[r]:
                r+=1
                max_profit = max(max_profit, prices[r]-prices[l])
            while prices[l]>prices[r]:
                l+=1
        
        return max_profit 

        