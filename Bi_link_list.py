class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Double_List(object):
    def __init__(self):
        self._head = Node(None)
        self._length = 0

    def is_empty(self):
        if self._length == 0:
            return True
        else:
            return False

    def travel(self):
        cur = self._head
        for i in range(self._length):
            print(cur.next.data, end=" ")
            cur = cur.next
        else:
            print(" ")

    def append(self, data):
        new_code = Node(data)
        cur = self._head
        for i in range(self._length):
            cur = cur.next
        else:
            new_code.prev = cur
            cur.next = new_code
            self._length += 1

    def insert(self, pos, data):
        if isinstance(pos, int):
            if pos < 0:
                dl.insert(0, data)
            elif pos > self._length:
                dl.append(data)
            else:
                new_code = Node(data)
                cur = self._head
                for i in range(self._length):
                    if i == pos:
                        new_code.prev = cur
                        new_code.next = cur.next
                        cur.next = new_code
                        new_code.next.prev = new_code
                        self._length += 1
                        return
                    else:
                        cur = cur.next
        else:
            print("pos数据无效！")

    def remove(self, data):
        if self.is_empty():
            print("list is empty")
        else:
            cur = self._head
            for i in range(self._length):
                if cur.next.data == data:
                    if cur.next.next is None:
                        cur.next = None
                    else:
                        cur.next = cur.next.next
                        # 2.让中间节点后的节点的prev指向中间节点的前节点
                        cur.next.prev = cur
                        # 更新链表长度
                    self._length -= 1
                    return
                else:
                    cur = cur.next
            else:
                print("{} is not in".format(data), end="")


if __name__ == "__main__":
    print("尾部 插 入： ", end="")
    dl = Double_List()
    for i in range(10):
        dl.append(i)
    dl.travel()

    print("任意位置插入：", end="")
    dl.insert(-100, "a")
    dl.insert(6, "x")
    dl.insert(100, "z")
    dl.travel()

    print("删除 节 点 ：", end="")
    dl.remove("a")
    dl.remove("x")
    dl.remove("z")
    dl.travel()
    dl.remove("xxx")
    dl.travel()
