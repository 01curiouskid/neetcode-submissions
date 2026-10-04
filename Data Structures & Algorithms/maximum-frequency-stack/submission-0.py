class FreqStack:

    def __init__(self):
        self.cnt=defaultdict(int)
        self.maxCnt=0
        self.stacks=defaultdict(list)

    def push(self, val: int) -> None:
        self.cnt[val] = 1+self.cnt[val]
        self.maxCnt=max(self.maxCnt, self.cnt[val])
        self.stacks[self.cnt[val]].append(val)

    def pop(self) -> int:
        res = self.stacks[self.maxCnt].pop()
        self.cnt[res] -=1
        if not self.stacks[self.maxCnt]:
            self.maxCnt -=1
        return res

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()