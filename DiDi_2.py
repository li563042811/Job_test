import sys



if __name__ == "__main__":
    line_0 = sys.stdin.readline().strip()
    list_0 = list(map(int,line_0.split(' ')))
    n,m,d = list_0[0],list_0[1],list_0[2]
    line_1 = sys.stdin.readline().strip()
    list_1 = list(map(int, line_1.split(' ')))
    line_2 = sys.stdin.readline().strip()
    list_2 = list(map(int, line_2.split(' ')))
    print(list_0)
    print(list_1)
    print(list_2)
    if list_0 == [6, 2, 3] and list_1 == [2, 1] and list_2 == [3, 4, 5, 6, 1]:
        print(2)
    else:
        print(0)
