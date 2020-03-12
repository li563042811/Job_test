'''
又到了丰收的季节，恰逢小易去牛牛的果园里游玩。
牛牛常说他对整个果园的每个地方都了如指掌，小易不太相信，所以他想考考牛牛。
在果园里有N堆苹果，每堆苹果的数量为ai，小易希望知道从左往右数第x个苹果是属于哪一堆的。
牛牛觉得这个问题太简单，所以希望你来替他回答。

输入描述:
第一行一个数n(1 <= n <= 105)。
第二行n个数ai(1 <= ai <= 1000)，表示从左往右数第i堆有多少苹果
第三行一个数m(1 <= m <= 105)，表示有m次询问。
第四行m个数qi，表示小易希望知道第qi个苹果属于哪一堆。

输出描述:
m行，第i行输出第qi个苹果属于哪一堆。

输入例子1:
5
2 7 3 4 9
3
1 25 11

输出例子1:
1
5
3
'''
import sys

def Sum_n(n,l=[]):
    result = 0
    for i in range(n):
        result+=l[i]
    return result

def Find(num,list_=[]):
    left,right = 0,len(list_)-1
    if num <= 0 or num >list_[-1]:
        return None
    while left < right :
        mid = (left+right)//2
        if list_[mid] == num:
            return mid+1
        elif list_[mid] < num:
            left = mid+1
        elif list_[mid] > num:
            right = mid
    return  right+1

def CalApple(n,l_1,m,l_2):
    l_cal = []
    result = []
    for i in range(1,n):
        l_1[i] += l_1[i-1]
    # for i in range(n):
    #     l_cal.append(Sum_n(i+1,l_1))
    for j in range(m):
        result.append(Find(l_2[j],l_1))
    return result


if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    line_1 = sys.stdin.readline().strip()
    l_1 = list(map(int,line_1.split(' ')))
    m = int(sys.stdin.readline().strip())
    line_2 = sys.stdin.readline().strip()
    l_2 = list(map(int,line_2.split(' ')))
    result = CalApple(n, l_1, m, l_2)
    for i in range(len(result)):
        print(result[i])

