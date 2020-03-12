import sys

def Fx(x,y,step):
    next = [[0,1],[1,0],[0,-1],[-1,0]]
    if x==finalx and y ==finaly:
        if step<min:
            min = step
            flag=1
    return

def main_(n,m,x=0,y=0,a=[]):
    mim = 9999999
    step = 0
    flag = 0
    next = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    for k in range(3):
        tx = x + next[k][0]
        ty = y + next[k][1]
        if tx<1 or tx>n or ty<1 or ty>m:
            continue
        if a[tx][ty] == '.' and book[tx][ty] ==0:
            book[tx][ty] = 1
            Fx(tx,ty,step+1)
            book[tx][ty] = 0

def HeFa(input_list=[]):
    temp_list = [[0,0],[0,0]]
    temp_list[0][0] = input_list
    temp_list[0][1] = input_list
    temp_list[1][0] = input_list
    temp_list[1][1] = input_list

def Pinjie_Migong(migong=[]):
    result = []
    for i in range(len(migong)):
        temp_migong = migong[i]


if __name__ == "__main__":
    T = int(sys.stdin.readline().strip())
    nm = []
    migong = [[] for i in range(T)]
    for i in range(T):
        line_0 = sys.stdin.readline().strip()
        list_0 = list(map(int,line_0.split(' ')))
        nm.append(list_0)
        print(nm)
        for j in range(nm[i][0]):
            temp = sys.stdin.readline().strip()
            temp_l = list(temp.split(' '))
            migong[i].append(temp_l)
    startx,starty,finalx,finaly = 1,1,1,1
    book = []
    book[startx][starty] = 1
    Fx[startx,starty,0]
    for i in range(T):
        main_(nm[i][0],nm[i][1],)




