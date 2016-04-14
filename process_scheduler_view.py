from tkinter import *
from tkinter import ttk

number_of_rows = 0
process_list = []

def add_process_row(frame):
    global number_of_rows
    number_of_rows += 1
    row_num = number_of_rows

    burst_time = IntVar()
    priority = IntVar()
    arr_time = IntVar()

    ttk.Label(frame, text="Process " + str(row_num)).grid(row=row_num, column=0) 
    ttk.Entry(frame, textvariable=burst_time).grid(row=row_num, column=1)
    ttk.Entry(frame, textvariable=priority).grid(row=row_num, column=2)
    ttk.Entry(frame, textvariable=arr_time).grid(row=row_num, column=3)
    frame.pack()

    global process_list
    process_list.append([burst_time, priority, arr_time])

def parse_and_run_alg(radio_val, time_quanta):
    global process_list
    
    try:
        quanta = time_quanta.get()
    except ValueError:
        print ("quanta is incorrect")

    print(process_list)

    int_list = []
    for row in process_list:
        inner_list = []
        for column in row:
            try:
                current = column.get()
                inner_list.append(current)
            except ValueError:
                inner_list.append(0)
        int_list.append(inner_list)

    if radio_val == 0:
        print ("FCFS")
    elif radio_val == 1:
        print ("SJF")
    elif radio_val == 2:
        print ("priority")
    elif radio_val == 3:
        print ("RR")
    

def create_scheduler_view(proc_sched):
    radio_var = IntVar()
    ttk.Label(proc_sched, text="Algoritm:").pack(anchor = W)

    #algorithm type setup
    ttk.Radiobutton(proc_sched, text="First Come First Serve", variable=radio_var, value=0).pack(anchor = W)
    ttk.Radiobutton(proc_sched, text="Shortest Job First", variable=radio_var, value=1).pack(anchor = W)
    ttk.Radiobutton(proc_sched, text="Priority", variable=radio_var, value=2).pack(anchor = W)
    ttk.Radiobutton(proc_sched, text="Round Robin", variable=radio_var, value=3).pack(anchor = W)

    #time quantum setup
    q_frame = ttk.Frame(proc_sched)
    ttk.Label(q_frame, text="Time Quanta:").grid(row=0, column=0)
    quanta_var = IntVar()
    ttk.Entry(q_frame, textvariable=quanta_var).grid(row=0, column=1)
    q_frame.pack()

    #process info setup
    s_frame = ttk.Frame(proc_sched)
    ttk.Label(s_frame, text="Process").grid(row=0, column=0) 
    ttk.Label(s_frame, text="Burst Time").grid(row=0, column=1)
    ttk.Label(s_frame, text="Priority").grid(row=0, column=2)
    ttk.Label(s_frame, text="Arrival Time").grid(row=0, column=3)
    s_frame.pack()

    add_process_row(s_frame)

    #button setup
    b_frame = ttk.Frame(proc_sched)
    ttk.Button(b_frame, text="Add", command=lambda: add_process_row(s_frame)).grid(row=0, column=0)
    ttk.Button(b_frame, text="Run", command=lambda: parse_and_run_alg(radio_var.get(), quanta_var)).grid(row=0, column=1)
    b_frame.pack()
    
