import sys

def Find_minnum(list,sum,num):

    if len(list)==0:
        return -1
    if sum in list:
        num+=1
    if sum < list[0] and sum != 0:
        return -1
    if sum>list[0] and sum<list[-1]:
        for i in range(len(list)):
            if list[i]>sum:
                list.pop(i)
    if sum > list[-1]:
        list_last=list[-1]
        num+=1
        return Find_minnum(list,sum-list_last,num)
    return num

if __name__ == "__main__":
    line=sys.stdin.readline().strip()
    list = list(map(int, line.split(',')))
    sum = int(sys.stdin.readline().strip())
    list.sort()
    print(Find_minnum(list,sum,0))