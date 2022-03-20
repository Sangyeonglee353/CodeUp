# 6079 : [기초-종합] 언제까지 더해야 할까?(py)
n = int(input())
sum = 0
k = 1
while sum <= 1000:
    sum += k
    k = k + 1
    if sum >= n:
        print(k - 1)
        break