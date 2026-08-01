import heapq as h

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ## Definitions
        heap = [(nums[i], i) for i in range(k)]
        out = []
        ## Windows
        l=0
        r=k-1
        h.heapify_max(heap)
        while r<len(nums)-1:
            while heap[0][1]<l: h.heappop_max(heap)
            out.append(heap[0][0])
            l+=1
            r+=1
            h.heappush_max(heap, (nums[r], r))
        while heap[0][1]<l: h.heappop_max(heap)
        out.append(heap[0][0])
        return out


