>>> from tkinter import *
>>> master = Tk()
>>> myText =StringVar();
>>> Label(master,text="first number").grid(row=0,sticky=W)
>>> Label(master,text="second number").grid(row=1,sticky=W)
>>> Label(master,text="sum").grid(row=3,sticky=W)
>>> e1 = Entry(master)
>>> e2 = Entry(master)
>>> e1.grid(row=0, column=1)
>>> e2.grid(row=1, column=1)
>>> result = Label(master, text=" ")
>>> b = Button(master, text="calculate")
>>> b.grid(row=0,column =2, columnspan=2, rowspan=2)
>>> mainloop()