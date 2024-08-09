#실습3
class Calculator:
    def __init__(self):
        self.value = 100

    def sub(self, value):
        self.value -= value
        return self.value

class LimitCalculator(Calculator):
    def sub(self, value):
        super().sub(value) #부모의 value를 가져옴
        if self.value < 0:
            self.value = 0
        return self.value

lc = LimitCalculator()
print(lc.sub(20))
print(lc.sub(90))