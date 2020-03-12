import sys

class Solution:
    def solution(self, n):
        result = 0
        i = 1
        if n<= 1:
            return n
        while (i*(i+1)/2 <= n):
            result += i*i
            i+=1
        result += i*(n - i*(i-1)/2)
        return int(result)

if __name__ == "__main__":
    line = int(sys.stdin.readline().strip())
    print(Solution().solution(line))




