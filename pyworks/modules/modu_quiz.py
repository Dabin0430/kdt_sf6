# 실습1
import random
'''
import random

idx1 =[]

for i in range(6):
    idx = random.randint(1, 100)
    idx1.append(idx)

idx1.sort()
print(idx1)
'''
# 실습 2
lotto = []
'''
for i in range(6):
    print(len(lotto))#중복확인
    n = random.randint(1, 45) #랜덤 요소
    if n not in lotto: #중복 방지
        lotto.append(n)
'''
while len(lotto) < 6:
    print(len(lotto))  # 중복확인
    n = random.randint(1, 45)  # 랜덤 요소
    if n not in lotto:  # 중복 방지
        lotto.append(n)

lotto.sort() #오름 차순
print(lotto)

