# 6064 : [기초-3항연산] 정수 3개 입력받아 가장 작은 값 출력하기(설명)(py)
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
d = (a if a<b else b) if ((a if a<b else b)<c) else c
print(int(d))