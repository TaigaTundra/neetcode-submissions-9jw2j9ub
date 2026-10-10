class Solution:
    def isValid(self, s: str):
        pairs = {
            '(':')',
            '{':'}',
            '[':']'
        }
        stk = []

        for brace in s:
            if brace in pairs:
                stk.append(brace)
            elif not stk or pairs[stk.pop()] != brace:
                return False
        return not stk

