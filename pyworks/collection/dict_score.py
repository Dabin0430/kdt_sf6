#학생 3명의 성적 통계
student = [
    {"name": "이대한", "kor": 90, 'math': 85},
    {"name": "박민국", "kor": 80, 'math': 75},
    {"name": "임지능", "kor": 95, 'math': 90},
]

#print(student)
#print(student[-1])
'''
print("♣ 개인별 평균 점수 ♣")
print("이름   국어 수학 평균")
for std in student:
    sum_score = std["kor"] + std["math"] #개인별 총점
    avg_score = sum_score / 2
    print(f'{std["name"]} {std["kor"]} {std["math"]} {avg_score : .2f}')
'''

print("♣ 과목별 총점과 평균 ♣")
kor = []
math = []
for std in student:
    subject_sum = sum({std['kor']})
    kor.append(subject_sum)

for std in student:
    subject_sum = sum({std['math']})
    math.append(subject_sum)

sum_kor = sum(kor)
sum_math = sum(math)
avg_kor = sum(kor) / 3
avg_math = sum(math) / 3
print(f'국어 총점: {sum_kor}\n'
      f'수학 총점: {sum_math}\n'
      f'국어 평균: {avg_kor:.2f}\n'
      f'수학 평균: {avg_math:.2f}')
