class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        f = [1]
        b = [1]
        n = len(nums)
        for i in range(n):
            f.append(nums[i]*f[i])
            b.append(b[i] * nums[n-1-i])
        ret = []
        for i in range(n):
            ret.append(f[i] * b[n-1-i])
        return ret
            
