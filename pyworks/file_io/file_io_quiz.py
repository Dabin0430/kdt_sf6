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



# 실습 2(실습 3과 연결됨)

try:
    with open("source/member.txt", "w") as f:
        for i in range(3):
            name = input("이름을 입력하세요: ")
            pw = input("비밀번호를 입력하세요: ")
            f.write(f'{name} {pw}\n')
except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")


try:
    with open("./source/member.txt", "r") as f:
        member = f.read()
        print(member)
except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")

# 실습 3
# 로그인
name = input('이름 입력: ')
pw = input('비밀번호 입력: ')
user = name + " " + pw + "\n"

with open("./source/member.txt", "r") as f:
    member_list = f.readlines()  # 데이터를 리스트로 반환
    # print(member_list)

    # 상태 변수 - True/Fasle
    sw = False  # 상태 초기화 False임
    for member in member_list: #리스트를 순회하면서
        # 파일에 있는 member의 name, pw와 입력한 user의 name, pw가 일치하면
        if member == user:
            sw = True  #상태를 True로 저장

    if sw:  #sw == True
        print("로그인 성공!")
    else:  #sw == False
        print("로그인 실패!")
