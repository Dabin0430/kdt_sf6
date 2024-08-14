# #실습 1
# f = open("c:/pyfile/gugudan.txt", "w")
#
# for i in range(1,10):
#     for j in range(1,10):
#         f.write(f'{i} * {j} = {i * j}\n')
#     f.write("\n")
# f.close()
#
#
# f = open("c:/pyfile/gugudan.txt", "r")
# print(f.read())
# f.close()



#실습2
try:
    count = 0
    with open("./output/member.txt", 'a') as f:
        while True:
            name = input(f'{count+1}번째 회원의 이름을 입력해주세요: ')
            pw = input(f'{count+1}번째 회원의 패스워드를 입력해주세요: ')
            count += 1
            if count >= 3:
                break
            f.write(name)
            f.write('\n')
            f.write(pw)
            f.write('\n')
except ValueError:
    print("잘못 입력하셨습니다")