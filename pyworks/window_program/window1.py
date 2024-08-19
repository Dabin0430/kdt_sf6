# 윈도우 생성 - tkinter
# 체계 : root=Tk() > Frame > Label, Button > mainloop()
from tkinter import *
# 루트 생성
root = Tk()
root.title("처음 만든 윈도우")
#창크기(가로x세로)
root.geometry("300x100")

#콤포넌트(구성요소-레이블, 버튼, 입력상자)
#출력(Label)
#배치 - pack(side=left): 한줄을 차지(LEFT, RIGHT, TOP, BOTTOM)
#grid(): 자유롭게 배치(E, W, S, N)
# Label(root, text="안녕하세요~").grid(row=0, column=0)
lbl = Label(root, text='안녕하세요')
lbl.grid(row=0, column=0, sticky=W)
btn = Button(root, text='확인', font=('맑은고딕', 10))
btn.grid(row=1, column=0)
root.mainloop()