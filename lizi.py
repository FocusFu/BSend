from Tkinter import *
def aaa():
    global root
    #filename = 'E:\obj.gif'
    #img = PhotoImage(file=filename)
    label = Label(root, text = 'aaa')
    label.pack()
root = Tk()
b= Button(root ,text ='a',command =aaa)
b.pack()
root.mainloop()