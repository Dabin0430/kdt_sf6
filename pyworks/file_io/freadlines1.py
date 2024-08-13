# readlines() - 데이터를 리스트로 반환

try:
    f = open("./source/season0.txt", 'r')
    seasons = f.readlines()  # 데이터가 seasons 리스트 변수에 저장됨
    print(seasons)
    print(seasons[1])
    print(seasons[-1])
    print(seasons[1:3])

    # 전체 출력
    for season in seasons:
        print(season.strip())

    f.close()
except FileNotFoundError as msg:
    #print("파일을 찾을 수 없습니다.")
    # 내부의 에러메시지 보고 싶을때
    print(msg)