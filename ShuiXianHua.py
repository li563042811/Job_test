import sys

def strnum(num):
    s = [int(char) for char in str(num)]
    return s

def ShuiXian(list_0 = []):
    left,right = list_0[0],list_0[1]
    strtemp = []
    for i in range(left,right+1):
        return


if __name__ == "__main__":
    inputlist = []
    for line in sys.stdin:
        #line_0 = line.readline().strip()
        list_0 = list(map(int,line.split(' ')))
        inputlist.append(list_0)
    print(inputlist)
    print(strnum(inputlist[0][0]))