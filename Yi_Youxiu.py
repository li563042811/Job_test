import sys

def MinDict(n,num=[]):
    left,right = 0,n-1
    for i in range(n):
        for j in range(i,n):
            temp = num[i] + num[j]
            if temp % 2 == 1:
                if num[i] > num[j]:
                    num[i], num[j] = num[j], num[i]
    return num


if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    line = sys.stdin.readline().strip()
    num = list(map(int,line.split(' ')))
    result = MinDict(n,num)
    result = map(str,result)
    print(" ".join(result))

