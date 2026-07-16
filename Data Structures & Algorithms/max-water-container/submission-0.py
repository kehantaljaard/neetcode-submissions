class big:
    def __init__(self, l, r, v):
        self.l=l
        self.r=r
        self.v = v

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        m = big(l, r, (r-l) * min(heights[l], heights[r]))
        while l<r:
            s = l if heights[l]<heights[r] else r
            if s==l: l+=1
            elif s==r: r-=1 
            vol = (r-l) * min(heights[l], heights[r])
            if vol > m.v: m.l, m.r, m.v = l, r, vol
        return m.v          