class Solution:
    def isValid(self, s: str):
        pairs = {
            '(':')',
            '{':'}',
            '[':']',
        }     

        stk = []
        for bracket in s:
            if bracket in pairs:
                stk.append(bracket)
            else:
                if not stk or pairs[stk.pop()] != bracket:
                    return False 
        
        return not stk
