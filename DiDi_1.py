import sys

def Calculate(inputlist = []):
    str = ''
    for i in range(len(inputlist)):
        str = str+inputlist[i]
    result = eval(str)
    return result

def Ex(a,b,l = []):
    temp = l.copy()
    temp[a],temp[b] = temp[b],temp[a]
    return temp

def Exchange(inputlist = []):
    sum_0 = Calculate(inputlist)
    length = len(inputlist)
    if length <= 2:
        return inputlist
    for j in range(0,length-1,2):
        for i in range(0,length-1,2):
            temp_list = inputlist.copy()
            if int(inputlist[i]) > int(inputlist[i+2]) and sum_0 == Calculate(Ex(i,i+2,temp_list)):
                inputlist[i],inputlist[i+2] = inputlist[i+2],inputlist[i]
    return inputlist

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    line = sys.stdin.readline().strip()
    list_0 = line.split(' ')
    result = []
    result = Exchange(list_0)
    for element in result:
        print(element+' ')
