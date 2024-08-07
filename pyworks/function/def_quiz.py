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
def get_price(x, y):
    if x * y < 20000:
        return x * y + 2500
    else:
        return x * y
box1 = get_price(10000, 3)
box2 = get_price(5000, 3)

print(f'상품1 가격: {format(box1, ',d')}원')
print(f'상품2 가격: {format(box2, ',d')}원')#무조건 , 천단위로 찍힘