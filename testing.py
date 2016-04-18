from tkinter import *
from tkinter import ttk

def cbQuit():
    exit()

def draw(can):
    can.create_line(0, 0, 200, 100)
    can.create_rectangle((150, 150, 250, 250))
    
def pushfunc(var1, var2, var3):
    var3.set(var2.get())
    var2.set(var1.get())
    var1.set("")

root = Tk()
root.title("Operating Systems Sample Tk Program Stuff 2.0 - Return of Tk")
root.geometry("600x400")

notebook = ttk.Notebook(root)

one = ttk.Frame(notebook)
two = ttk.Frame(notebook)
three = ttk.Frame(notebook)

notebook.add(one, text="Tab one")
notebook.add(two, text="Tab two")
notebook.add(three, text="Tab three")

notebook.pack()


quitlabel = Label(one, text = "to exit:").pack(side = LEFT)
quitbutton = Button(one, text = "ok", command = cbQuit).pack(side = LEFT)

can = Canvas(two, width=300, height=300)
can.pack()
bcan = Button(two, text = "Place", command=lambda: draw(can)).pack()

var1 = StringVar()
e1 = Entry(three, width = 6, textvar = var1).pack()
var2 = StringVar()
e2 = Entry(three, width = 6, textvar = var2).pack()
var3 = StringVar()
e3 = Entry(three, width = 6, textvar = var3).pack()

bpush = Button(three, text = "push", command=lambda: pushfunc(var1, var2, var3)).pack()

root.mainloop()
