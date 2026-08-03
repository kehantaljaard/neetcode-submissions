class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        out = [0]*len(temperatures)
        for i, n in enumerate(temperatures):

            while stack and n > stack[-1][0]: # first element of the tuple
                top = stack.pop()
                out[top[1]] = i-top[1]
            stack.append((n, i))
        return out


