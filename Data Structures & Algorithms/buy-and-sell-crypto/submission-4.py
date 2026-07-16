class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        f = [0] * len(prices)
        b = [0] * len(prices)        
        ret=0
        for i in range(len(prices)):
            if i == 0: f[i] = prices[i]
            else: f[i] = min(f[i-1], prices[i])
            j = len(prices)-1-i
            if j == len(prices)-1: b[j] = prices[j]
            else: b[j] = max(b[j+1], prices[j])
            v = b[i] - f[i]
            ret = max(v, ret)
        return ret
         

