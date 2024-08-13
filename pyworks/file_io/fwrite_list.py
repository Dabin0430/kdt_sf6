# 리스트 자료 쓰기
# 상대 경로 - source 폴더

f = open("./source/season.txt", 'w')
season = ['봄', '여름', '가을', '겨울']
for i in season:
    f.write(i + " ")

f = open("./source/season.txt", 'r')

data = f.read()
print(data)

f.close()