'''
今天上课，老师教了小易怎么计算加法和乘法，乘法的优先级大于加法，但是如果一个运算加了括号，那么它的优先级是最高的。例如：
1
2
3
4
1+2*3=7
1*(2+3)=5
1*2*3=6
(1+2)*3=9
现在小易希望你帮他计算给定3个数a，b，c，在它们中间添加"+"， "*"， "("， ")"符号，能够获得的最大值。

输入描述:
一行三个数a，b，c (1 <= a, b, c <= 10)

输出描述:
能够获得的最大值

输入例子1:
1 2 3

输出例子1:
9
'''

import sys

def CanMax(a,b,c):
    s = {1,2}
    if a in s and b in s:
        return 3*c
    elif b in s and c in s:
        return 3*a
    elif a == 1 or b ==1:
        return (a+b)*c
    elif c == 1:
        return a*(b+c)
    else:
        return a*b*c

if __name__ == "__main__":
    line = sys.stdin.readline().strip()
    list_1 = list(map(int,line.split(' ')))
    a,b,c = list_1[0],list_1[1],list_1[2]
    print(CanMax(a,b,c))
