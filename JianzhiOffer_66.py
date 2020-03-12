'''
地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，但是不能进入行
坐标和列坐标的数位之和大于k的格子。 例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。但是，它不能进入方
格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？
'''

import sys

class Solution:
    def movingCount(self,threshold,rows,cols):
        board = [[0 for _ in range(cols)] for _ in range(rows)]
        def block(r,c):
            num = sum(map(int,str(r)+str(c)))
            return num>threshold
        class content:
            acc = 0
        def travel(r,c):
            if not (rows>r>=0 and cols>c>=0):
                return
            if board[r][c]!=0 :
                return
            if board[r][c] == -1 or block(r,c):
                board[r][c] = -1
                return
            board[r][c] = 1
            content.acc += 1
            travel(r + 1, c)
            travel(r - 1, c)
            travel(r, c + 1)
            travel(r, c - 1)
        travel(0,0)
        return content.acc

if __name__=="__main__":
    k = int(sys.stdin.readline().strip())
    m = int(sys.stdin.readline().strip())
    n = int(sys.stdin.readline().strip())
    print(Solution().movingCount(k,m,n))