# 다중 if 실습

score = float(input("점수를 입력해주세요: "))
grade = "" #빈 문자열
if  score >= 90:
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
