import sys

def money(m,a=[],target=0,result = 0):
    if target < a[0]:
        return -1
    if target == a[0]:
        return result+1
    while target >= a[m] and m <= len(a)-1 and m >= 0:
        num = target // a[m]
        result += num
        left = target % a[m]
        if left < a[m]:
            m-=1
        return money(m,a[:m],left,result)

if __name__ == "__main__":
    line = sys.stdin.readline().strip()
    a=list(map(int,line.split(',')))
    target = int(sys.stdin.readline().strip())
    a = sorted(a)
    print(money(len(a)-1,a,target,0))