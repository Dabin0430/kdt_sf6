# 실습1

import random

idx1 =[]

for i in range(4):
    idx = random.randint(1, 100)
    idx1.append(idx)

idx1.sort()
print(idx1)