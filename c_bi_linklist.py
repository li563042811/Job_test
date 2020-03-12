# import sys
#
# def find(n,score):
#     percent = n // 1000
#     if percent < 1:
#         percent = 1
#     temp = sorted(score,reverse=True)
#     return temp[:percent]
#
# if __name__ =="__main__":
#     n = int(sys.stdin.readline().strip())
#     score = []
#     for i in range(n):
#         m = int(sys.stdin.readline().strip())
#         score.append(m)
#     result = find(n,score)
#     for element in result:
#         print(element)


# File Name : 反转双向链表.py

import sys

class Node(object):
    def __init__(self, value):
        self.next = None

        self.pre = None

        self.value = value

    def reverseList(self, head_node):
        pre = None

        while head_node != None:
            next = head_node.next

            head_node.next = pre

            head_node.pre = next

            pre = head_node

            head_node = next

        return pre

if __name__ =='__main__':
    line = sys.stdin.readline().strip()
    list_ = list(map(int,line.split(' ')))
    result = list_[::-1]
    for i in result:
        print(i,end=' ')

