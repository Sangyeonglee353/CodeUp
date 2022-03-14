# 6044 : [기초-산술연산] 정수 2개 입력받아 자동 계산하기(py)
a, b = input().split()
x = int(a) + int(b)
print(x)

y = int(a) - int(b)
print(y)

u = int(a) * int(b)
print(u)

v = int(a) // int(b)
print(v)

w = int(a) % int(b)
print(w)

h = int(a) / int(b)
print(format(h, '.2f'))