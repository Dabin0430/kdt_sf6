#실습1
#1
student = {}
print(type(student))
#2
student['Alice'] = "85"
student['Bob'] = "90"
student['Charlie'] = "95"
print(student)
#3
student['David'] = "80"
print(student)
#4
student['Alice'] = "88"
print(student)
#5
student.pop('Bob')
print(student)
#6
for key in student:
    print(key, ":", student[key])
#print(f"{key}의 점수는 {student.get{key}")
