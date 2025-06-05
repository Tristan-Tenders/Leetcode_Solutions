class Solution(object):
    def isValid(self, s):
        stack =[]
        matching = {')': '(', ']': '[', '}': '{'}
        for char in s:
            if char in ('{','[','('):
                stack.append(char)
            else:
                if not stack or stack[-1] != matching[char]:
                    return False
                stack.pop()
        if len(stack) == 0:
            return True
        else:
           return False

                    
