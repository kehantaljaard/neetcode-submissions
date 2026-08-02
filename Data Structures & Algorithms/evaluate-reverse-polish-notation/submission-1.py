class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        signs = ["+", "-", "*", "/"]
        for i in tokens:
            if i in signs:
                b = int(stack.pop())
                a = int(stack.pop())
                if i == "+": stack.append(str(a+b))
                if i == "-": stack.append(str(a-b))
                if i == "*": stack.append(str(a*b))
                if i == "/": stack.append(str(int(a/b)))
            else:
                stack.append(i)
                
        return int(stack.pop())
