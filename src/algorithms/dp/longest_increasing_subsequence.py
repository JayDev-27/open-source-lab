"""LIS dynamic programming algorithm."""
def lis(arr):
    n = len(arr)
    if n == 0: return 0
    dp = [1] * n
    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
    return max(dp)
