from tkinter import *
from tkinter import ttk
from process_scheduler_view import *

#set up the window
root = Tk()
root.title("Operating System Simulation")
root.geometry("500x300")

#set up the tab structure
notebook = ttk.Notebook(root)

#set up each fo the tabs and add them 
proc_sched = ttk.Frame(notebook) 
mem_man = ttk.Frame(notebook)
page_rep = ttk.Frame(notebook) 

notebook.add(proc_sched, text = "Process Scheduler")
notebook.add(mem_man, text = "Memory Managment Unit")
notebook.add(page_rep, text = "Page Replacement")

#set up the view for the process scheduler tab
create_scheduler_view(proc_sched)

#set up the view for the memory management unit tab

l2 = ttk.Label(mem_man, text="In Memory Management Unit")
l2.pack()

#set up the view for the page replacement tab
l3 = ttk.Label(page_rep, text="In Page Replacement")
l3.pack()

#proc_sched.pack() 
#mem_man.pack()
#page_rep.pack() 

notebook.pack(side=TOP)

root.mainloop()
