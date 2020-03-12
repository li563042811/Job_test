# def Solution(stri):
#     number = 0
#     l = list(stri)
#     l1 = []
#     l1.append(stri)
#     for i in range(len(l)):
#         l.append(l[0])
#         l.pop(0)
#         string = str(l)
#         if string not in l1:
#             l1.append(string)
#             number+=1
#     return number
#
# stri = input()
# print(Solution(stri))

#coding=utf-8
# 本题为考试多行输入输出规范示例，无需提交，不计分。

# import tensorflow as tf
# import matplotlib as plt
# import sklearn
# #import keras
import sys
def Solution(a,b):
    array = b
    k = a[1]
    num = False
    min_num = 0
    for i in range(k):
        for j in range(len(array)):
            if array[j] == 0:
                array.pop(j)
                continue
            else:
                num = True
        if num == False:
            return 0
        min_num = min(array)
        print(min_num)
        for i in range(len(array)):
            array[i] -= min_num
        print(array)

def Find_minnum(list,sum,num):

    if len(list)==0:
        return -1
    if sum in list:
        num+=1
    if sum < list[0] and sum != 0:
        return -1
    if sum>list[0] and sum<list[-1]:
        for i in range(len(list)):
            if list[i]>sum:
                list.pop(i)
    if sum > list[-1]:
        list_last=list[-1]
        num+=1
        return Find_minnum(list,sum-list_last,num)
    return num

#第一行输入列表去掉逗号
#第二行输入一个int
# if __name__ == "__main__":
#     line=sys.stdin.readline().strip()
#     list = list(map(int, line.split(',')))
#     sum = int(sys.stdin.readline().strip())
#     list.sort()
#     print(Find_minnum(list,sum,0))

# 多行输入，排除逗号空格
if __name__ == "__main__":
    l_0 = []
    for line in sys.stdin:
        line = line.strip()
        line = map(int,line.split(','))
        l_0.extend(line)
    print(l_0)


# if __name__ == "__main__":
#     #读取第一行的n
#     l1 = []
#     l2 = []
#     n = int(sys.stdin.readline().strip())
#     for i in range(n):
#         # 读取每一行
#         line = sys.stdin.readline().strip()
#         l1.append(int(line))
#     for j in range(n):
#         line2 = sys.stdin.readline().strip()
#         l2.append(int(line2))
#     list = l1
#     sum = 12[0]
#     Find_minnum(list,sum)






#import sys
# for line in sys.stdin:
#     a = line.split()
#     print (int(a[0]) + int(a[1]))
# for line in sys.stdin:
#     b = line.split()
#     print(b)
