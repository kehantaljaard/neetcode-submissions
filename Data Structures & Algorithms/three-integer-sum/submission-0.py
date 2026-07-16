class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ret = []
        for i, a in enumerate(nums):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            if l>=r or l==i:
                continue
            cur = []
            while l<r:
                if -a == nums[l] + nums[r]:
                    cur.append([nums[l],nums[r]])
                    l+=1
                    r-=1
                elif a+nums[l]+nums[r]<0:
                    while(nums[l+1] == nums[l]): l+=1
                    l+=1
                elif a+nums[l]+nums[r]>0:
                    while(nums[r-1] == nums[r]): r-=1
                    r-=1
            for i in cur:
                ret.append([a, i[0], i[1]])
        return ret
            
