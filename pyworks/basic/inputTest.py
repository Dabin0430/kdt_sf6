이름 = input('이름을 입력하세요.')
나이 = int(input('나이를 입력하세요.'))
print(f'안녕하세요! {이름}님 ({나이}세)')


이름 = input('이름을 입력하세요.')
출생년도 = int(input('태어난 년도를 입력하세요'))
올해년도 = int(input('올해 년도를 입력하세요.'))
나이 = 올해년도 - 출생년도 + 1
print(f' 올해는 {올해년도}년, {이름}님의 나이는 {나이}세 입니다')
