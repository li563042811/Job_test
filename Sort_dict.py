dict_data = {6:9,10:5,3:11,8:2,7:6}

#字典按key排序
test_1 = sorted(dict_data.keys())
print(test_1)
#字典按value排序
test_2 = sorted(dict_data.items(),key=lambda x:x[1])
print(test_2)

l_1 = [1,2,3,4,5]
l_2 = ['1','2','3','4','5']
l_1 = map(str,l_1)
print(" ".join(l_1))

import itertools
#全排列
print("全排列：")
permutation = []
for i in itertools.permutations('abcd',4):
    permutation.append(i)
#print(permutation)

#全排列
def perm(l):
    if len(l)<=1:
        return [l]
    r = []
    for i in range(len(l)):
        s=l[:i]+l[i+1:]
        p = perm(s)
        for x in p:
            r.append(l[i:i+1]+x)
    return r

print(perm([1,2,3,4]))


dic = {"apple":"苹果","banana":"香蕉"}
print(dict.fromkeys("banana","菠萝"))
print(dict.fromkeys("xyz",["苹果","橘子"]))

#浅拷贝
lst1 = ["金毛狮王", "紫衫龙王", "青翼蝠王", "白眉鹰王",["张无忌","赵敏","周芷若"]]
lst1_poor = lst1.copy()
lst1_poor[0]= "jmsw"
lst1_poor[4][0]= "zwj"
lst1[0] = "jmsw"
print(lst1)
print(lst1.copy())
print(lst1[:])

#深拷贝
import copy
lst2 = copy.deepcopy(lst1)
lst2[0] = "jmsw"
print(lst2)
print(lst1)
print(id(lst1))
print(id(lst2))
