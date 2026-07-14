class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        d = 1
        for i in s:
            newd = 1
            j = i
            while(j+1 in s):
                newd+=1
                j+=1
            if newd > d: d=newd
        return d
