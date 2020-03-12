import sys

def Jaccard(m,n):
    s_1 = set(m)
    s_2 = set(n)
    return len(s_1 & s_2)/len(s_1 | s_2)


def ASR(list_1,list_2):
    result = [0]*len(list_1)
    for i in range(len(list_1)):
        max_j = 0
        for j in range(len(list_2)):
            temp_j = Jaccard(list_1[i],list_2[j])
            if temp_j >= max_j:
                max_j = temp_j
                result[i] = j
    return result


if __name__ == "__main__":
    line_1 = sys.stdin.readline().strip()
    list_1 = line_1.split(',')
    line_2 = sys.stdin.readline().strip()
    list_2 = line_2.split(',')
    x = int(sys.stdin.readline().strip())
    result = ASR(list_1,list_2)
    r_str = []
    for element in result:
        r_str.append(str(element))
    print(','.join(r_str))
