class Solution:
    def isValid(self, s: str):
        pairs = {
            '(':')',
            '{':'}',
            '[':']',
        }     
        stack = []
        for brace in s:
            if brace in pairs:
                stack.append(brace)
            else:
                if not stack or pairs[stack.pop()] != brace:
                    return False   
        return not stack
