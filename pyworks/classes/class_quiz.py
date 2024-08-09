# 실습 1 - 사칙연산 클래스 만들기

import sys
class Calculator:
     # 생성자 메서드(함수)
     def __init__(self, x, y):
         self.x = x
         self.y = y

     def div(self):
             if self.y == 0:
                 print("0으로 나눌수 없음")
                 return sys.exit(0)
             else:
                 return self.x / self.y

     def add(self):
         return self.x + self.y  # return 값에서 연산을 바로함

     def sub(self):
         return self.x - self.y

     def mul(self):
         return self.x * self.y


c1 = Calculator(1, 2)  # 만들어진 클래스에 값을 넣어줘야함

print(c1.div())




# 실습2 - SuperMarket 클래스
class SuperMarket:
    def __init__(self, location, name, product, customer):
        self.location = location #위치
        self.name = name #가게이름
        self.product = product #파는 물건
        self.customer = customer #고객의 수

    def show_info(self):
        print(f'위치: {self.location}, 이름: {self.name}, 상품: {self.product}, 고객수: {self.customer}')

    def print_location(self):
        print(self.location)

    def change_category(self,a):
        self.product = a
        print(self.product)
    def show_list(self):
        print(self.product)

    def enter_customer(self):
        self.customer += 1

products = [
    SuperMarket("마포구 염리동", "마켓온", "음료", 12)
]

products[0].print_location()
products[0].change_category("과자")
products[0].show_info()

'''
class SuperMarket:
    def __init__(self, location, name, product, customer):
        self.location = location # 위치
        self.name = name  # 가게 이름
        self.product = product # 파는 물건
        self.customer = customer # 고객의 수

    def print_location(self):
        print(f'위치: {self.location}')

    def change_category(self, another_product):
        self.product = another_product

    def show_list(self):
        print(f'상품: {self.product}')

    def enter_customer(self):
        self.customer += 1  #self.customer = self.customer + 1

    def show_info(self):
        print(f'위치: {self.location}, 이름: {self.name}, '
              f'상품: {self.product}, 고객수: {self.customer}')


super1 = SuperMarket("마포구 염리동", "마켓온", "과일", 10)
super1.print_location()
super1.change_category("음료")
super1.show_list()
super1.enter_customer() #고객 1 들어옴
super1.enter_customer() #고객 1 들어옴
super1.show_info()
'''
