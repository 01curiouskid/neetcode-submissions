class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.stones=[-stone for stone in stones]
        heapq.heapify(self.stones)
        while len(self.stones)>1:
            stone1=-heapq.heappop(self.stones)
            stone2=-heapq.heappop(self.stones)
            print(stone1, stone2)
            if stone1>stone2:
                heapq.heappush(self.stones, stone2-stone1)
        return -self.stones[0] if self.stones else 0