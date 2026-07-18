from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:        
        l, r = 0, 0
        ret =0 
        win = defaultdict(int)
        win[s[l]]+=1
        while r<len(s)-1:
            n = r-l+1 - max(win.values(), default=0)
            if n<=k:
                r+=1
                win[s[r]]+=1
            while r-l+1 - max(win.values(), default=0) >k:
                win[s[l]]-=1
                l+=1
            ret = max(r-l+1, ret)
        return ret
                