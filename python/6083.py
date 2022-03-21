# 6083 : [기초-종합] 빛 섞어 색 만들기(설명)(py)
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
num = 0
for i in range(a):
    for j in range(b):
        for k in range(c):
            print(i, j, k)
            num += 1
print(num)