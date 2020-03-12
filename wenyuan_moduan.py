def Longest(l = []):
    result = 1
    i = 0
    while i <len(l)-2:
        if l[i]+l[i+l[i]]<l[i+1]+l[i+1+l[i+1]]-1:
            i = i+1+l[i+1]
        else:
            i = i+l[i]
        result+=1
    return result

l = [2,3,1,1,4]
print(Longest(l))

