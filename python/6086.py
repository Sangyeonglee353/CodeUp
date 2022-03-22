# 6086 : [기초-종합] 거기까지! 이제 그만~(설명)(py)
n = int(input())
i = 1
s = 0
while True:
    s += i
    i += 1
    if s>=n:
        break
print(s)