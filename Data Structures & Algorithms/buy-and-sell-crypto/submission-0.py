class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        f = [0] * len(prices)
        b = [0] * len(prices)
        for i in range(len(prices)):
            if i == 0: f[i] = prices[i]
            else: f[i] = min(f[i-1], prices[i])
        ret=0
        for i in range(len(prices)-1, -1, -1):
            if i == len(prices)-1: b[i] = prices[i]
            else: b[i] = max(b[i+1], prices[i])
            v = b[i] - f[i]
            ret = max(v, ret)
        return ret
         

