from tkinter import *


def click():
    name = entry.get()
    label.config(text=name)

root = Tk()
root.title("이름 입력")
# 창크기(가로x세로+x좌표+y좌표)
root.geometry("400x200+500+500")
# 프레임
frame = Frame(root)
frame.pack() #한 줄을 차지

# 컴포넌트
Label(frame, text="이름: ").grid(row=0, column=0)
#입력상자(Entry())
entry = Entry(frame)
entry.grid(row=0, column=1)
#columnspan = 열병합
Button(frame, text='확인', command=click).grid(row=1, columnspan=2)
label = Label(frame, width=25, height=3)
label.grid(row=2, columnspan=2)
root.mainloop()