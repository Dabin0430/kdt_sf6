#실습1(정수의 합 계산)
'''
num = int(input("어디까지 계산할까요?: "))
total = 0

for i in range(1, num+1):
    total += i
print(f'1부터 {num}까지의 합: {total}')

홀수의 합계
num = int(input("몇까지의 합을 계산할까요?")
total = 0
for i in range(1, num + 1):
    if i % 2 != 0:
        total += i
'''
#실습2(입력한 숫자만큼 카운트하고 "발사" 출력
'''
second = int(input("몇 초?: "))

for i in range(second, 0, -1):
    print(i, end = " ")
print("발사")

'''
#실습3(구구단 만들기)

num = int(input("몇단을 출력할까요?"))
total = ""
for i in range(0, 10, 1):
    total = num * i
    print(f'{num} * {i} = {total}')