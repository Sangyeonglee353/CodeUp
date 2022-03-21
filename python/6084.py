# 6084 : [기초-종합] 소리 파일 저장용량 계산하기(py)
h, b, c, s = input().split()
h = int(h)
b = int(b)
c = int(c)
s = int(s)
value = (h * b * c * s) / 8 / 1024 / 1024
value = round(float(value), 1)
print("{0} MB".format(value))
