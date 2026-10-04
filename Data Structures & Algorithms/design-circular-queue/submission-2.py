class ListNode:
    def __init__(self,val,nxt=None):
        self.val=val
        self.next=nxt

class MyCircularQueue:

    def __init__(self, k: int):
        self.space=k
        self.start=ListNode(0)
        self.end=self.start

    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False
        cur=ListNode(value)
        if self.isEmpty():
            self.start.next=cur
            self.end=cur
        else:
            self.end.next=cur
            self.end=cur
        self.space-=1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        if self.start.next==self.end:
            self.start=self.end=ListNode(0)
        else:
            self.start.next=self.start.next.next
        self.space+=1
        return True
    def Front(self) -> int:
        if self.isEmpty(): return -1
        return self.start.next.val

    def Rear(self) -> int:
        if self.isEmpty(): return -1
        return self.end.val

    def isEmpty(self) -> bool:
        return self.start.next==None
        

    def isFull(self) -> bool:
        return self.space==0
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()