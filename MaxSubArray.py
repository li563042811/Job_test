import sys

def max_(a,b):
    if a>b:
        return a
    else:return b

def MaxSub(array):
    result = 0
    dp = [0]*len(array)
    dp[0] = array[0]
    for i in range(1,len(array)):
        dp[i] = max_(array[i],dp[i-1]+array[i])
    result = max(dp)
    return result


if __name__ =="__main__":
    array = []
    line = sys.stdin.readline().strip()
    line = list(map(int,line.split(',')))
    # for line in sys.stdin:
    #     line = line.strip()
    #     line = list(map(int,line.split(',')))
    #     array.extend(line)
    #print(array)
    print(MaxSub(line))