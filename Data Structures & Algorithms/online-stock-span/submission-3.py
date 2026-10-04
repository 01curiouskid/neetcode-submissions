class StockSpanner:

    def __init__(self):
        self.stack=[]
        self.index=0


    def next(self, price: int) -> int:
        if not self.stack:
            self.stack.append((self.index,price))
            self.index+=1
            return 1
        if self.stack[-1][1]>price:
            self.stack.append((self.index,price))
            self.index+=1
            return 1
        while self.stack and self.stack[-1][1]<=price:
            self.stack.pop()
        self.stack.append((self.index,price))
        self.index+=1
        return (self.stack[-1][0]-self.stack[-2][0]) if len(self.stack)>1 else self.index

        

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)