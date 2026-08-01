from collections import defaultdict
from typing import DefaultDict        

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        s1dic = defaultdict(int)
        for i in s1:
            s1dic[i]+=1

        comp = defaultdict(int)
        l=0
        r=len(s1)-1
        for i in range(0, r+1):
            comp[s2[i]]+=1
        if s1dic == comp: return True
        while r < len(s2)-1:
            comp[s2[l]]-=1
            if comp[s2[l]] ==0: del comp[s2[l]]
            l+=1
            r+=1
            comp[s2[r]]+=1
            if s1dic == comp: return True
        return False
            


            

        
        