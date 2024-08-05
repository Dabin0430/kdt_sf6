# 구구단 3단
'''
3 X 1 = 3
3 X 2 = 6
3 X 3 = 9
...
3 X 8 = 24
3 X 9 = 27

dan = int(input("단을 입력해주세요: "))
for i in range(1, 10):
    print(f'{dan} X {i} = {dan*i}')
'''
# 전체 구구단(중첩 for문)
for i in range(2, 10): #행 - 단
    for j in range(1, 10):
        print(f'{i} * {j} = {i * j}')
    print()
