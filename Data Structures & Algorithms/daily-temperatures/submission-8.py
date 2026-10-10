class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stk = []  
        
        for i in range(n - 1, -1, -1):
            while stk and temperatures[i] >= temperatures[stk[-1]]:
                stk.pop()
            if stk:
                res[i] = stk[-1] - i
            stk.append(i)
            
        return res
        