from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in nums:
            count[i] = 1 + count.get(i, 0)
        bucket = [[] for _ in range(len(nums)+ 1)]
        for i, n in count.items():
            bucket[n].append(i)
        ret = []
        for i in range(len(nums), 0, -1):
            for n in bucket[i]:
                ret.append(n)
                k-=1
                if k==0: break
        return ret

            

                


