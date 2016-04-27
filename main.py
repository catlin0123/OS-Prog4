from tkinter import *
from tkinter import ttk
from process_scheduler_view import *
from mem_management_view import *
from page_replacement_view import *

#set up the window
root = Tk()
root.title("Operating System Simulation")
root.geometry("1000x800")

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
create_mem_management_view(mem_man)

#set up the view for the page replacement tab
create_page_replacement_view(page_rep)

#proc_sched.pack() 
#mem_man.pack()
#page_rep.pack() 

notebook.pack(fill=BOTH, expand=1)

root.mainloop()
