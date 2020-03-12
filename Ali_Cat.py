import sys
import numpy as np

# 编辑距离
def edit_distance(word1, word2):
    len1 = len(word1)
    len2 = len(word2)
    dp = np.zeros((len1 + 1, len2 + 1))
    for i in range(len1 + 1):
        dp[i][0] = i
    for j in range(len2 + 1):
        dp[0][j] = j
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            delta = 0 if word1[i - 1] == word2[j - 1] else 1
            dp[i][j] = min(dp[i - 1][j - 1] + delta, min(dp[i - 1][j] + 1, dp[i][j - 1] + 1))
    return dp[len1][len2]

def TCat(l_1,l_2,t):
    result = 0
    for i in range(len(l_1)):
        for j in range(len(l_2)):
            if edit_distance(l_1[i],l_2[j]) <= t:
                result += 1
    return result


if __name__ == "__main__":
    t = int(sys.stdin.readline().strip())
    minS = int(sys.stdin.readline().strip())
    maxS = int(sys.stdin.readline().strip())
    line_1 = sys.stdin.readline().strip()
    list_A = line_1.split(',')
    line_2 = sys.stdin.readline().strip()
    list_B = line_2.split(',')
    print(TCat(list_A,list_B,t))