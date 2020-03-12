import sys

def Quanpailie(n,l=[]):
    num = 1+n
    result = []
    for i in range(n):
        result.append(num-l[i])
    return result

if __name__ == "__main__":
    # n = int(sys.stdin.readline().strip())
    # line = sys.stdin.readline().strip()
    # list_1 = list(map(int,line.split(" ")))
    # result = Quanpailie(n,list_1)
    # result = map(str,result)
    # print(" ".join(result))
    n = input()
    m = input()
    print("n: "+ str(n))
    print("n(0): " + str(n[0]))
    print("type of n :" + str(type(n)))
    print("m: "+ str(m))