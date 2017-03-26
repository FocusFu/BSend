import Tkinter
import tkMessageBox
top = Tkinter.Tk()
def dele(root,a):

    root.create_image(64,64,image=a)
C = Tkinter.Canvas(top, bg="blue", height=1000, width=600)
filename = Tkinter.PhotoImage(file = "E:\obj.gif")
image = C.create_image(64,64,image=filename)
a = Tkinter.PhotoImage(file="test2\obj2__31.gif")
b = Tkinter.Button(top, text='gg', command=lambda:dele(C,a))
b.pack()
C.pack()
top.mainloop()