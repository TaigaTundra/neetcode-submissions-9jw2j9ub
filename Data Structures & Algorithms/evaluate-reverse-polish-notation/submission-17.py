class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        res = 0 
        for tk in tokens:
            if tk == "+":
                b = int(stk.pop())
                a = int(stk.pop())
                res = a+b
                stk.append(res)
            elif tk == "-":
                b = int(stk.pop())
                a = int(stk.pop())
                res = a-b
                stk.append(res)
            elif tk == "*":
                b = int(stk.pop())
                a = int(stk.pop())
                res = a*b
                stk.append(res)
            elif tk == "/":
                b = int(stk.pop())
                a = int(stk.pop())
                res = int(a/b)
                stk.append(res)
            else:
                stk.append(int(tk))
        return stk.pop()
    
