from tkinter import *

root = Tk()
root.geometry('400x400')
root.title('查询等级')
Label(root, text='输入内容:', font=('Arial', 14)).pack()
Text(root, bg="white", fg="black").pack()
# Text(root, width=10, height=5).pack()
root.mainloop()
