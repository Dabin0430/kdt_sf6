# time 모듈
# time.time() - 1970.1.1 자정이후 부터 시간을 초로 반환
import time
import math

print(time.time()) #17억초
# 일로 환산
day = math.floor(time.time()) / (24 * 60 *  60)
print(day)
# 년으로 환산
year = math.floor(time.time()) / (365 * 24 * 60 *  60)
print(year)

# # time.sleep(1) - 1초 간격으로 대기
# for i in range(1, 11):
#     print(i)
#     time.sleep(0.5) #0.5초 간격으로 숫자 출력

# 수행(실행) 시간 측정
start = time.time() #시작 시간
#print(start)

for i in range(1000000):
    print(i)
    #time.sleep(1)

end = time.time()
print("수행 시간: " + str(end-start) + "초")