# 실습 5

#sum()
#print(sum([1, 2, 3])) #6
#print(max([1, 2, 3])) #3

#1
input_num = input("숫자 여러 개 입력: ").split(" ")
numbers = [] #숫자를 저장할 리스트
for i in input_num:
    numbers.append(int(i))
print(numbers)
#2
max1 = max(numbers)
min1 = min(numbers)
print(f'가장 큰값: {max1}')
print(f'가장 작은값: {min1}')
#3
numbers.remove(max(numbers))
numbers.remove(min(numbers))
mean = sum(numbers) / len(numbers)
print(f'나머지 값의 평균: {mean}')