#print("Hello~")
#인사하는 함수 - greet
def greet():
    print("안녕~") #지역 영역

def greeting(name):
    print("안녕~", name)

#메인 영역(실행 영역)
greet() #함수 호출

greeting("현수") #name = "현수"
greeting("민우")

def get_gugu(dan):
    for i in range(1, 10):
        print(f'{dan} x {i} = {dan * i}')

def add(x, y):
    total = x + y
    print("더하기:", total)
add(10, 10)
#구구단 호출
#get_gugu(20) #dan = 4
