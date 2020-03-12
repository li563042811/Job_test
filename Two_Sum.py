import sys

def Two_Sum(nums,target):
    l = len(nums)
    if l < 1:
        return
    hash_num = {}
    result = []
    for ind,num in enumerate(nums):
        hash_num[num] = ind
    for ind_,num_ in enumerate(nums):
        #del hash_num[num_]
        temp = hash_num.get(target-num_)
        if temp is not None and temp != ind_:
            result.append([ind_,temp])
    return hash_num,result

if __name__ == "__main__":
    line = sys.stdin.readline().strip()
    nums = list(map(int,line.split(',')))
    target = int(sys.stdin.readline().strip())
    hash_num,result = Two_Sum(nums,target)
    print(hash_num)
    print(result)
