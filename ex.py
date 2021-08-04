n = int(input())
dp = []
sum = n * (n + 1) // 2
if sum % 2 == 1:
    print(0)
    exit()
for i in range(sum // 2 + 10):
    dp.append(0)

dp[0] = 1
for i in range(1, n + 1):
    j = sum // 2
    while j >= i:
        dp[j] += dp[j - i]
        j -= 1

# for i in range(1, sum // 2 + 1):
    # print(dp[i], end=' ')
# print()
print(int((dp[sum // 2] // 2) % (10**9 + 7)))