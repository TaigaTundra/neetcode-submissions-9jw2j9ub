class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            '(':')',
            '[':']',
            '{':'}'
        }
        stack =[]

        for bracket in s:
            if bracket in pairs:
                stack.append(bracket)
            elif len(stack) == 0 or bracket != pairs[stack.pop()]:
                return False
        return not stack
                

  