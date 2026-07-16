class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        f = [0] * len(prices)
        b = [0] * len(prices)
        for i in range(len(prices)):
            if i == 0: f[i] = prices[i]
            else: f[i] = min(f[i-1], prices[i])
        ret=0
        for i in range(len(prices)):
            j = len(prices)-1-i
            if j == len(prices)-1: b[j] = prices[j]
            else: b[j] = max(b[j+1], prices[j])
            v = b[j] - f[j]
            ret = max(v, ret)
        # for j in range(len(prices)-1, -1, -1):
        #     if j == len(prices)-1: b[j] = prices[j]
        #     else: b[j] = max(b[j+1], prices[j])
        #     v = b[j] - f[j]
        #     ret = max(v, ret)
        return ret
         

