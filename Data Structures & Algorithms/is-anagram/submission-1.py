class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        count = {}
        for l in s:
            if l in count:
                count[l]+=1
            else: count[l]=1
        for l in t:
            if l in count:
                count[l]-=1
                if count[l] == 0:
                    del count[l]
            else: return False
        if len(count) == 0: return True
        return False

        