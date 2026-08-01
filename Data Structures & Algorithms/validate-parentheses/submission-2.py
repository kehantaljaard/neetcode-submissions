class Solution:
    def isValid(self, s: str) -> bool:
        op = ['(', '[', '{']
        cl = [')', ']', '}']
        stack = []
        for i in s:
            if i in op:
                stack.append(i)
            elif i in cl:
                if not stack: return False
                temp = stack.pop()
                if not ((temp == '(' and i ==')') 
                or (temp == '[' and i ==']')
                or (temp == '{' and i =='}')):
                    return False
        return not stack

