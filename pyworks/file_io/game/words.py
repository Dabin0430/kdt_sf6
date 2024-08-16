# 영어 단어장 만들기

import random

with open("words.txt", 'w') as f:
    word = ['sky', 'earth', 'moon', 'flower', 'tree', 'apple',
        'mountain', 'garlic', 'onion', 'potato']

    for i in word:
        f.write(i + " ")


with open("words.txt", "r") as f:
  # 상태 변수 - True/Fasle
    data = f.read().split() #공백 문자로 구분
    print(data)
    print(random.choice(data))
