# 실습 1 - 사칙연산 클래스 만들기

import sys
class Calculator:
     # 생성자 메서드(함수)
     def __init__(self, n1, n2):
         self.n1 = n1
         self.n2 = n2

     def div(self):
             if self.n2 == 0:
                 print("0으로 나눌수 없음")
                 return sys.exit(0)
             else:
                 return self.n1 / self.n2


c1 = Calculator(1, 2)  # 만들어진 클래스에 값을 넣어줘야함

print(c1.div())

'''
     def add(self):
         return self.x + self.y #return 값에서 연산을 바로함

     def sub(self):
         return self.x - self.y

     def mul(self):
         return self.x * self.y
'''

