class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        '''
        n = len(cost)
        dp = [0] *(n+1)

        dp[2] = min(cost[0],cost[1])

        for i in range(3,n+1):
            dp[i] = min(dp[i-1] +cost[i-1],dp[i-2] +cost[i-2])
        
        return dp[-1]
        '''
        n = len(cost)
        curr,prev =0,0

        for i in range(2,n+1):
            old_curr = curr
            curr = min (curr +cost[i-1],prev +cost[i-2])
            prev = old_curr
        
        return curr
