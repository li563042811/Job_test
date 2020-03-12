import sys
import numpy


def largestRectangleArea(heights):
    heights.append(0)
    h = heights
        # 递增栈
    stack = []
        # 初始值
    res = 0
    for i, values in enumerate(h):
        while stack and values < h[stack[-1]]:
            remove_val = stack[-1]
                # stack要弹出最高值
            stack.pop(-1)
            if stack == []:
                begin = 0
            else:
                begin = stack[-1] + 1
            res = max(res, h[remove_val] * (i - begin))
        stack.append(i)
    return res
def MoreWater(height):
    height.append(0)
    stack = [-1]
    ans = 0
    for i in range(len(height)):
        while height[i] < height[stack[-1]]:
            h = height[stack.pop()]
            w = i - stack[-1] - 1
            ans = max(ans, h * w)
        stack.append(i)
    height.pop()
    return ans

def Water(a=[]):
    left,right = 0,len(a)-1
    result = a[0]
    while left < right:
        if a[left]<a[right]:
            if result < a[left]*(right - left):
                result = a[left]*(right - left)
            left += 1
        else:
            if result < a[right]*(right - left):
                result = a[right]*(right - left)
            right -= 1
    return result



# if __name__ == "__main__":
#     list_ = []
#     list_0 = []
#     while True:
#         list_0 = list_
#         line = sys.stdin.readline().strip('\n')
#         l = list(map(int,line.split(',')))
#         list_.extend(l)
#         if len(list_) <= len(list_0):
#             break
#     print(MoreWater(list_))

if __name__ == "__main__":
    a = []
    for line in sys.stdin:
        line = line.strip()
        line = list(map(int,line.split(' ')))
        a.extend(line)
    print(Water(a))


# if __name__ == "__main__":
#     line = sys.stdin.readline().strip()
#     list_ = []
#     while line:
#         list_.extend(list(map(int, line.split(","))))
#     print(list_)
#     print(largestRectangleArea(list_))
#     print(MoreWater(list_))
