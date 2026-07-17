class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cur = set()
        ret = 0
        l=0
        r=0
        for r in range(len(s)):
            while s[r] in cur:
                cur.discard(s[l])
                l+=1
            cur.add(s[r])
            nl = r-l+1
            ret = max(ret, nl)
        return ret




