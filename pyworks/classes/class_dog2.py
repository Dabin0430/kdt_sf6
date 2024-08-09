

class Dog:
    #tricks = []#클래스 변수  #위에서 사용하면 한번에 할당
    def __init__(self, name):
        self.name = name
        self.tricks = [] #이곳에서 사용하면 각 객체마다 할당
        print("생성자 메서드입니다.")

    def add_trick(self, trick):
        self.tricks.append(trick)

dog1 = Dog('John')
dog1.add_trick("몸 뒤집기")
print(dog1.tricks)

dog2 = Dog('Jerry')
dog2.add_trick("죽은척 하기")
print(dog2.tricks)