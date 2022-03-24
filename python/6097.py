# 6097 : [기초-리스트] 설탕과자 뽑기(py)
# 매트릭스 생성
h, w = map(int, input().split())
matrix = []
for i in range(h+1) :
    matrix.append([])
    for j in range(w+1) :
        matrix[i].append(0)

# 막대 입력
line_num = int(input())
for index in range(line_num):
    l, d, x, y = map(int, input().split())
    
    if d == 0:
        for col in range(l):
            matrix[x][y+col] = 1
    elif d == 1:
        for row in range(l):
            matrix[x+row][y] = 1
    else:
        print("error")

for t in range(1, h+1):
    for u in range(1, w+1):
        print(matrix[t][u], end=' ')
    print()


