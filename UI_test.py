#
from tkinter import *
from PIL import Image,ImageTk

root = Tk()
root.geometry('1200x600+150+100')
root.title('战场环境可视化界面')
root.resizable(False,False)

im = Image.open("C:\\Users\\li563042811\\Desktop\\yesanpo.png")
img = ImageTk.PhotoImage(im)
imLabel=Label(root,image=img).pack(side=RIGHT,expand=YES,fill=NONE)
photo = PhotoImage("C:\\Users\\li563042811\\Desktop\\yesanpo.png")
Lab =Label(root,text = '战场环境',compound='center',font = ('微软雅黑',15))
Lab.pack(side=LEFT,expand=YES,fill=Y)


root.mainloop()