#실습 1 정수 입력 받기 - 예외 처리


while True:
    try:
        num1 = int(input("숫자 입력: "))
        print(f'정수 입력 성공: {num1}')
        break
    except ValueError:
        print("정수가 아님! 정수를 입력해주세요")



