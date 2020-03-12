import sys

def Sum_List(input_list=[]):
    result = [0 for i in range(len(input_list))]
    for j in range(len(input_list)):
        n,m = input_list[j][0],input_list[j][1]
        result[j] = n
        for i in range(m-1):
            n =  pow(n,0.5)
            result[j] += n
    return result

if __name__ == "__main__":
    input_list = []
    for line in sys.stdin:
        l_0 = line.strip()
        l_1 = list(map(int,l_0.split(' ')))
        input_list.append(l_1)
    for i in range(len(input_list)):
        print("%.2f"%(Sum_List(input_list)[i]))