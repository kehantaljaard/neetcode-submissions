class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        signs = ["+", "-", "*", "/"]
        for i in tokens:
            if i in signs:
                b = int(stack.pop())
                print(f'popped {b}')
                a = int(stack.pop())
                print(f'popped {a}')
                if i == "+": 
                    print(f'{a}+{b}')
                    stack.append(str(a+b))
                if i == "-": 
                    print(f'{a}-{b}')
                    stack.append(str(a-b))
                if i == "*": 
                    print(f'{a}*{b}')
                    stack.append(str(a*b))
                if i == "/": 
                    print(f'{a}/{b}')
                    stack.append(str(int(a/b)))
            else:
                print(f'append {i}')
                stack.append(i)
        return int(stack.pop())
