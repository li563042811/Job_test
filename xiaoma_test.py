import sys
import numpy as np
def Max_num(T,K,N,array):
    result = []
    temp = 0
    num = 0
    if T == 0 :
        return None
    for i in range(T):
        if K[i] == 0:
            result[i] = array[i]
        else:
            while num < K[i]:
                for j in range(N[i]-1):
                    if array[i][j] < array[i][j+1]:
                        temp = array[i][j]
                        array[i][j] = array[i][j - 1]
                        array[i][j - 1] = temp
                        num += 1
                    else:
                        continue

            result.append(array[i])
    return result


if __name__ == "__main__":
    T = int(sys.stdin.readline().strip())
    K,N,array = [],[],[]
    for i in range(T):
        # 读取每一行
        K.append(int(sys.stdin.readline().strip()))
        N.append(int(sys.stdin.readline().strip()))
        line = sys.stdin.readline().strip()
        l = list(map(int, line.split()))
        array.append(l)
    result = np.array(Max_num(T, K, N, array))
    for i in range (T):
        print(result[i])


