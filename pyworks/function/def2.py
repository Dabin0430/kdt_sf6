#return이 있는 함수(반환값이 있음)

#매개변수 1개
#자기 자신을 곱하는 함수 - 제곱수 함수
def square(x):
    return x * x

def myabs(x):
    if x < 0:
        return -x
    return x

def mul(x, y):
    return x * y


print(myabs(-10))

#value = square(6) # return이 준 반환값은 value 저장
#print(value)

#절대값을 구하는 함수 - abs(x)
#print(abs(-10)) #10
#print(abs(10))

print(mul(5, 2))
value2 = mul(5, 2)
print(value2)

