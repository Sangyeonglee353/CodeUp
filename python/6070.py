# 6070 : [기초-조건/선택실행구조] 월 입력받아 계절 출력하기(설명)(py)
n = int(input())
if n//3 == 1:
    print("spring")
elif n//3 == 2:
    print("summer")
elif n//3 == 3:
    print("fall")
else:
    print("winter")
    
# def check(n):       
#     if n//3 == 1:
#         print("spring")
#     elif n//3 == 2:
#         print("summer")
#     elif n//3 == 3:
#         print("fall")
#     else:
#         print("winter")

# for i in range(1, 13):
#     check(i)