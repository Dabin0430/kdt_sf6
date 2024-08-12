import datetime
#날짜와 시간 모두 출력
#now = datetime.datetime.now()
now = datetime.datetime.today()
print(now)
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)

#날짜만 출력
print(f'{now.year}년 {now.month}월 {now.day}일')

#시간만 출력
print(f'{now.hour}시 {now.minute}분 {now.second}초')

#2023년 7월 31일 출력
the_day = datetime.date(2024, 7, 31)
print(the_day)

#오늘 날짜만 출력
today = datetime.date.today()
print(today)

print(" ★ 지금까지 몇 일? ★ ")
passed_time = today - the_day
#print(passed_time)
print(f'개강 이후 {passed_time.days}일 지났습니다.')

#추석까지 D-day 사용해서 구현
chuseok = datetime.date(2024, 9, 17)
d_day = chuseok - today
print(f'추석까지 {d_day.days}일 남았습니다.')
