import heapq


class MaxHeapObj(object):
    def __init__(self, val): self.val = val
    def __lt__(self, other): return self.val > other.val
    def __eq__(self, other): return self.val == other.val
    def __str__(self): return str(self.val)


class MinHeap(object):
    def __init__(self): self.h = []
    def push(self, x): heapq.heappush(self.h, x)
    def pop(self): return heapq.heappop(self.h)
    def get(self, i): return self.h[i]
    def len(self): return len(self.h)


class MaxHeap(MinHeap):
    def push(self, x): heapq.heappush(self.h, MaxHeapObj(x))
    def pop(self): return heapq.heappop(self.h).val
    def get(self, i): return self.h[i].val

# =================================Testing=======================================


minh = MinHeap()
maxh = MaxHeap()
# add some values
for num in range(5):
    maxh.push(num)
    minh.push(num)

print(minh.get(0))  # peek
print(maxh.get(0))  # peek

print(minh.pop())  # pop
print(maxh.pop())  # pop
