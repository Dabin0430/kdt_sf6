#기본 매개변수

def pr_str(txt, count=1): #=1을 넣는 이유는 아무것도 넣지 않았을때 돌아가게 만들기위해서 넣지 않았을경우 오류가 생김
    for i in range(count):
        print(txt)

pr_str('Hello', 3)