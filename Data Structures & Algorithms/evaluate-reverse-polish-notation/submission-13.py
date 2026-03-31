class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = 0
        stk = []
        for char in tokens:
            if char == '+':
                a = int(stk.pop())
                b = int(stk.pop())
                res = b + a
                stk.append(res)
            elif char == '-':
                a = int(stk.pop())
                b = int(stk.pop())
                res = b - a
                stk.append(res)
            elif char == '/':
                a = int(stk.pop())
                b = int(stk.pop())
                res = int(b / a)
                stk.append(res)
            elif char == '*':
                a = int(stk.pop())
                b = int(stk.pop())
                res = b * a
                stk.append(res)
            else:
                stk.append(int(char)) 
        return stk.pop()

        


        