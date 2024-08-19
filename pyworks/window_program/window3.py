# 체계 : root=Tk() > Frame > Label, Button > mainloop()
from tkinter import *

def click():
    #print("졸려~파이썬!")
    label.config(text="졸려~파이썬")

# 루트
root = Tk()
root.title("윈도우3")
root.geometry("200x150")
root.option_add('*Font', "맑은고딕 16")

#프레임
frame = Frame(root)
frame.pack()

Label(frame, text="Sleep~Python!!").grid(row=0, column=0)
#command속성: 버튼 눌렀을 때 함수를 실행 (click())
#함수 생성시점이 아닌 클릭했을 때 실행되어야 해서 괄호를 뺀다
Button(frame, text="확인", command=click).grid(row=1, column=0)
#출력레이블
label = Label(frame, text="Sleep~Python!!")
label.grid(row=2, column=0)


root.mainloop()