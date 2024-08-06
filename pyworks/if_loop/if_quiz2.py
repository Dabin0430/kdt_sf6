# 다중 if 실습
# 점수가 마이너스일 경우 "올바른 점수를 입력해주세요"

score = float(input("점수를 입력해주세요: "))
grade = "" #빈 문자열
'''
if score > 0:
    if score >= 90 and score <= 100:
        grade = "A"
    elif score >= 80 and score < 90:
        grade = "B"
    elif score >= 70 and score < 80:
        grade = "C"
    elif score >= 60 and score < 70:
        grade = "D"
    else:
        grade = "E"
    print(f'{grade}등급 입니다.')

else:
    print(f'올바른 점수를 입력해주세요')
'''

if score < 0:
    print(f'올바른 점수를 입력해주세요')
else:
    if score >= 90 and score <= 100:
        grade = "A"
    elif score >= 80 and score < 90:
        grade = "B"
    elif score >= 70 and score < 80:
        grade = "C"
    elif score >= 60 and score < 70:
        grade = "D"
    else:
        grade = "E"
    print(f'{grade}등급 입니다.')
