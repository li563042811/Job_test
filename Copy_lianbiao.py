import sys

class RandomListNode:
     def __init__(self, x,next = None,random = None):
         self.label = x
         self.next = next
         self.random = random
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead ,cHead = RandomListNode(0)):
        # write code here
        if pHead == None:
            return cHead
        cHead.next = RandomListNode(0)
        cHead.random = RandomListNode(0)
        temp,tempHead = [],pHead
        temp.append(pHead.label)
        pHead = pHead.next
        temp.append(pHead.label)
        pHead = tempHead
        pHead = pHead.random
        temp.append(pHead.label)
        pHead = tempHead
        tempcHead = cHead
        cHead.label = temp.pop(0)
        cHead = cHead.next
        cHead.label = temp.pop(0)
        cHead = tempcHead
        cHead = cHead.random
        cHead.label = temp.pop(0)
        cHead = tempcHead
        self.Clone(pHead.next,cHead.next)
        self.Clone(pHead.random,cHead.random)
        return cHead


if __name__ == "__main__":
    pHead = RandomListNode(3)
    pHead.next = RandomListNode(1,RandomListNode(4),RandomListNode(5))
    pHead.random = RandomListNode(2,RandomListNode(6),RandomListNode(7))
    Head = Solution().Clone(pHead)
    print(Head.label)
    Head = Head.random
    print(Head.label)