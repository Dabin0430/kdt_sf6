#global - 전역변수임을 알려주는 키워드
#전역변수는 값을 유지하고 공유함, 프로그램이 종료되면 소멸

def one_up():
    global x
    x += 1
    return x

x = 2 #전역변수
print(one_up()) #1
print(one_up()) #2
print(one_up()) #3
print(x)