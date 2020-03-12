'''
小易觉得高数课太无聊了，决定睡觉。不过他对课上的一些内容挺感兴趣，所以希望你在老师讲到有趣的部分的时候叫醒他一下。你知道了小易对一堂课每分钟知识点的感兴趣程度，并以分数量化，以及他在这堂课上每分钟是否会睡着，你可以叫醒他一次，这会使得他在接下来的k分钟内保持清醒。你需要选择一种方案最大化小易这堂课听到的知识点分值。

输入描述:
第一行 n, k (1 <= n, k <= 105) ，表示这堂课持续多少分钟，以及叫醒小易一次使他能够保持清醒的时间。
第二行 n 个数，a1, a2, ... , an(1 <= ai <= 104) 表示小易对每分钟知识点的感兴趣评分。
第三行 n 个数，t1, t2, ... , tn 表示每分钟小易是否清醒, 1表示清醒。

输出描述:
小易这堂课听到的知识点的最大兴趣值。

输入例子1:
6 3
1 3 5 2 5 4
1 1 0 1 0 0

输出例子1:
16
'''
import sys

def CalInterest(score=[],sleep=[]):
    result = 0
    for i in range(len(sleep)):
        if sleep[i] == 1:
            result += score[i]
    return result

def MaxInterest(n,k,score=[],sleep=[]):
    InterestScore = []
    temp = []
    for i in range(n-k+1):
        for j in range(k):
            temp.append(sleep[i+j])
            sleep[i+j]=1
        InterestScore.append(CalInterest(score,sleep))
        for m in range(k):
            sleep[i+m]=temp[m]
        temp = []
    return max(InterestScore)

def CalKscore(score,sleep,m,k):
    result = 0
    for i in range(k):
        if sleep[m+i]==0:
            result+=score[m+i]
    return result

def MaxInterest_(n,k,score=[],sleep=[]):
    result = []
    sum = 0
    for i in range(n-k+1):
        if sleep[i]==0:
            result.append(CalKscore(score,sleep,i,k))
        continue
    for j in range(n):
        if sleep[j]==1:
            sum+=score[j]
    return max(result)+sum


if __name__ == "__main__":
    line_1 = sys.stdin.readline().strip()
    l_1 = list(map(int,line_1.split(' ')))
    line_2 = sys.stdin.readline().strip()
    l_2 = list(map(int, line_2.split(' ')))
    line_3 = sys.stdin.readline().strip()
    l_3 = list(map(int, line_3.split(' ')))
    n,k = l_1[0],l_1[1]
    score = l_2
    sleep = l_3
    print(MaxInterest_(n,k,score,sleep))
