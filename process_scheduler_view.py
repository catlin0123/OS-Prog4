from tkinter import *
from tkinter import ttk

"""
def add_process_row(frame):
    add_process_row.num_rows++
    
add_process_row.num_rows = 0
""" 


def create_scheduler_view(proc_sched):
    s_radio_var = IntVar()
    s_l1 = ttk.Label(proc_sched, text="Algoritm:")
    s_l1.pack(anchor = W)

    #algorithm type setup
    s_r1 = ttk.Radiobutton(proc_sched, text="First Come First Serve", variable=s_radio_var, value=0)
    s_r2 = ttk.Radiobutton(proc_sched, text="Shortest Job First", variable=s_radio_var, value=1)
    s_r3 = ttk.Radiobutton(proc_sched, text="Priority", variable=s_radio_var, value=2)
    s_r4 = ttk.Radiobutton(proc_sched, text="Round Robin", variable=s_radio_var, value=3)
    s_r1.pack(anchor = W)
    s_r2.pack(anchor = W)
    s_r3.pack(anchor = W)
    s_r4.pack(anchor = W)

    s_l2 = ttk.Label(proc_sched, text="Time Quanta:")
    s_l2.pack(anchor = E)

    s_e1 = ttk.Entry(proc_sched, width=10)
    s_e1.pack()

    s_b1 = ttk.Button(proc_sched, text="Add")
    s_b1.pack()

    s_frame = ttk.Frame(proc_sched)
    s_l3 = ttk.Label(proc_sched, text="Process")
    s_l3.pack() #change to a grid
    s_l4 = ttk.Label(proc_sched, text="BurstTime")
    s_l4.pack() #change to a grid
    s_l5 = ttk.Label(proc_sched, text="Priority")
    s_l5.pack() #change to a gird
    s_l6 = ttk.Label(proc_sched, text="Arrival Time")
    s_l6.pack() #change to a grid

#    add_process_row(s_frame)

    s_b2 = ttk.Button(proc_sched, text="Run")
    s_b2.pack() 
