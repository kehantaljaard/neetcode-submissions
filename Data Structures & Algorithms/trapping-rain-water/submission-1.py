class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        f =[0]*len(height)
        b =[0]*len(height)
        for i, n in enumerate(height):
            if i==0:
                f[i] = n
            else:
                f[i] = max(n, f[i-1])
        for i in range(len(height)-1, -1, -1):
            if i==len(height)-1:
                b[i] = height[i]
            else: 
                b[i] = max(height[i], b[i+1])
        ret = 0
        for i in range(1, len(height)-1, 1):
            n = min(f[i-1], b[i+1]) - height[i]
            ret += n if n>= 0 else 0
        return ret