#바이너리 파일(binary file) 읽고 쓰기
#mode: 쓰기('wb'), 읽기('rb')
#바이너리 기계어(0,1)로 변환하는 함수 -> encode()
#기계어를 문자로 변환하는 함수 -> decode()

with open("./output/data.bin", "wb") as f:
    txt = "드론이 날아간다. "
    # f.write(txt) #TypeError str->object
    f.write(txt.encode())

with open("./output/data.bin", "rb") as f2:
    data = f2.read()
    print(data)
    print(data.decode())