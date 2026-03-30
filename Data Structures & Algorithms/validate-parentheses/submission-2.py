class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            '(' : ')',
            '[' : ']',
            '{' : '}',
        }
        stack = []


        for bracket in s:
            if bracket in pairs:
                stack.append(bracket)
            elif len(stack) == 0 or pairs[stack.pop()] !=bracket:
                return False
        return not stack
        
        