f = open("c:/pyfile/gugudan1.txt", "w")

for i in range(2, 10): #행 - 단
    for j in range(1, 10):
        f.write(f'{i} * {j} = {i * j}\n')
    f.write('\n')

f.close()
