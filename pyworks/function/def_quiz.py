#실습1
'''
def same(x, y):
    if x == y:
        return x * y
    else:
        return x + y
n1 = same(2, 2)
n2 = same(2, 3)

print(f'결과(곱): {n1}\n'
      f'결과(합): {n2}')
'''
#실습2
'''
def get_price(x, y):
    if x * y < 20000:
        return x * y + 2500
    else:
        return x * y
box1 = get_price(10000, 3)
box2 = get_price(5000, 3)

print(f'상품1 가격: {format(box1, ',d')}원')
print(f'상품2 가격: {format(box2, ',d')}원')#무조건 , 천단위로 찍힘

#실습4
def times():
    count = 0
    for i in range(1, 31):
        if i % 3 == 0:
            print(i,end=' ')
            count = count + 1
    print(f'\n3의 배수의 개수: {count}')

times()
'''

#실습3
vending_machine = ['게토레이', '레쓰비', '생수', '게토레이', '이프로', '생수']


def check_machine(): #남은 음료수를 출력하는 함수
    print("남은 음료는", vending_machine)


def is_drink(): #음료수가 있는지 확인하는 함수
    drink = input('마시고 싶은 음료는?')
    if drink in vending_machine:
        print(f'{drink}가 있습니다')
    else:
        print(f"{drink}는 지금 없네요")


def add_drink(): #음료를 추가하는 함수
    drink = input("추가할 음료수? ")
    vending_machine.append(drink)
    vending_machine.sort()# drink 추가


def remove_drink(): #음료를 제거하는 함수
    drink = input("삭제할 음료수? ")
    if drink in vending_machine:
        vending_machine.remove(drink)
        print("삭제 완료")
        print("남은 음료는", vending_machine)
    else:
        print("없음")
'''
while True:
    who = input("사용자 종류를 입력하세요: \n1.소비자 \n2.주인")
    if who == '1':
        drink = input("마시고 싶은 음료?")
        if drink in vending_machine:
            vending_machine.remove(drink)  # 입력된 drink 삭제
            print(f'{drink} 드릴게요')
        else:
            print(f"{drink}는 지금 없네요")
    elif who == '2':
        todo = input("할 일 선택(1.추가, 2.삭제) : ")
        if todo == '1':
            print("남은 음료는", vending_machine)
            drink = input("추가할 음료수? ")
            vending_machine.append(drink) #drink 추가
            vending_machine.sort() #오름차순 정렬
            print("추가 완료")
            print("남은 음료는", vending_machine)
        elif todo == '2':
            print("남은 음료는", vending_machine)
            drink = input("삭제할 음료수? ")
            if drink in vending_machine:
                vending_machine.remove(drink)
                print("삭제 완료")
                print("남은 음료는", vending_machine)
            else:
                print("없음")
'''
#remove_drink()
#add_drink()
#is_drink()

# 실습 3

vending_machine = ['게토레이', '레쓰비', '생수','게토레이', '이프로', '생수']

def check_machine(): # 남은 음료수를 출력하는 함수
    print("남은 음료수: ", vending_machine)

def is_drink():  # 음료수가 있는지 확인하는 함수
    if drink in vending_machine:
       return True
def add_drink():  # 음료수를 추가하는 함수
    vending_machine.append(drink)  # 입력된 drink 추가

def remove_drink():  # 음료수를 제거하는 함수
    vending_machine.remove(drink)

while True:
    who = input("사용자 종류를 입력하세요:\n1.소비자\n2.주인\n")
    if who == '1':
        drink = input("마시고 싶은 음료? ")
        if is_drink():
            print(drink, "드릴게요")
            remove_drink()
            check_machine()
        else:
            print(f"{drink}는 지금 없네요")
    elif who == '2':
        todo = input("할 일 선택(1.추가, 2.삭제) : ")
        print(todo)
        if todo == '1':
            check_machine()
            drink = input("추가할 음료수? ")
            add_drink()
            vending_machine.sort()  # 오름차순 정렬되면서 같은 값끼리 연결됨
            print("추가 완료")
            check_machine()
        elif todo == '2':
            check_machine()
            drink = input("삭제할 음료수? ")
            if is_drink():
                remove_drink()
                print("삭제 완료")
                check_machine()
            else:
                print("음료 없음")
