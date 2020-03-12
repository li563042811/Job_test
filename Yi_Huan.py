import sys

def BinHuan(l=[]):
    if len(l)<=2:
        return False
    for i in range(1,len(l)-1):
        if l[0]>=l[-1]+l[1] or l[-1]>=l[-2]+l[0]:
            return False
        if l[i]>=l[i-1]+l[i+1]:
            return False
        return True

def Huan(t,n_list=[],num_list=[]):
    if t<1 or t>10:
        return [False]
    result = []
    for i in range(len(n_list)):
        result.append(BinHuan(num_list[i]))
    return result


if __name__ == "__main__":
    t = int(sys.stdin.readline().strip())
    n_list = []
    num_list = []
    for i in range(t):
        n = int(sys.stdin.readline().strip())
        line = sys.stdin.readline().strip()
        list_ = list(map(int,line.split(' ')))
        n_list.append(n)
        num_list.append(list_)
    result = Huan(t,n_list,num_list)
    for i in range(len(result)):
        if result[i]==True:
            print("YES")
        else:
            print("NO")

