#자리 배치도
#고객수 - customer, 좌석열 - column, 행 - row
#나머지가 0일때 행의 수, 나머지가 0이 아닐때 행의 수 분기
customer = int(input("고객 수 입력: "))
column = int(input("좌석 열 수 입력: "))

if customer % column == 0:
    row = cutomer // column #몫
else:
    row = customer // column + 1

for i in range(0, row): #행
    for j in range(1, column + 1): #열
        num = i * column + j
        if num > customer:
            break
        print(num, end=' ')
    print()