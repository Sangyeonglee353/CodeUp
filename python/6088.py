# 6088 : [기초-종합] 수 나열하기1(py)
a, d, n = map(int, input().split())
s = a
for i in range(2, n+1):
    s += d
print(s)