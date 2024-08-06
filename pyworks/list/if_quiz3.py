#실습 4

age = int(input("나이를 입력해주세요: "))
card = input("결제 방법을 입력해주세요(카드 또는 현금만 입력: ")
fee = ''

if age < 8:
        fee = '무료'
elif age >= 8 and age < 14:
    if card == ("카드"):
        fee = 450
    else:
        fee = 450
elif age >= 14 and age < 20:
    if card == ("카드"):
        fee = 720
    else:
        fee = 1000
elif age >= 20 and age < 75:
    if card == ("카드"):
        fee = 1200
    else:
        fee = 1300
else:
    fee = '무료'

print(f'{age}세의 {card}요금은 {fee}원 입니다')

