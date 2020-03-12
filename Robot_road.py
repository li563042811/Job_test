#题目：机器人从一个大小为（m,n）的矩阵的左上角走到右下角一共有几种路径，只能向右或者向下。

def Robot_road(m,n,num = 0):
    if m == 1 or n == 1:
        num = num + 1
        return num
    if m == 2 and n == 2:
        return 2
    if  m>1:
        m = m - 1
        num = num + 1
        num = num + Robot_road(m,n,num)
    else:
        n = n - 1
        num = num + 1
        num = num + Robot_road(m,n,num)
    return num

print(Robot_road(1,2))
