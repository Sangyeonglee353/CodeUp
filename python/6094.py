# 6094 : [기초-리스트] 이상한 출석 번호 부르기3(py)
n = int(input())
a = input().split()
min = int(a[0])

for i in range(n):
    a[i] = int(a[i])

for i in range(n):
    if min > a[i]:
        min = a[i]

print(min)