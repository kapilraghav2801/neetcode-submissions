import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = nums
        
        #self.min_heap = []
        # for num in nums:
        #     heapq.heappush(self.min_heap, num)

        #     if len(self.min_heap) > k:
        #         heapq.heappop(self.min_heap)

        heapq.heapify(self.min_heap)

        while len(self.min_heap) > k:
            heapq.heappop(self.min_heap)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)

        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)


        return self.min_heap[0]

# """Brute force"""       
# class KthLargest:

#     def __init__(self, k: int, nums: List[int]):
#         self.k = k
#         self.nums = nums

#     def add(self, val):
#         self.nums.append(val)
#         self.nums.sort()
#         return self.nums[-self.k]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)