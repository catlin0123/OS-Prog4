from tkinter import *
from tkinter import ttk
from process_scheduler import *

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
    
def clear_process_row(s_frame):
    for w in s_frame.winfo_children():
        w.destroy()
        
    ttk.Label(s_frame, text="Process").grid(row=0, column=0) 
    ttk.Label(s_frame, text="Burst Time").grid(row=0, column=1)
    ttk.Label(s_frame, text="Priority").grid(row=0, column=2)
    ttk.Label(s_frame, text="Arrival Time").grid(row=0, column=3)
    
    global number_of_rows
    global process_list
    number_of_rows = 0
    process_list = []
    add_process_row(s_frame)
    

def parse_and_run_alg(radio_val, time_quanta, canvas, error):
    error.set("")
    global process_list
        
    int_list = []
    i = 1;
    for row in process_list:
        inner_list = []
        inner_list.append(i)
        for column in row:
            try:
                current = column.get()
                inner_list.append(current)
            except TclError:
                error.set("Process information is incorrect. All values must be integers.")
                return
        int_list.append(inner_list)
        i += 1

    if radio_val == 0:
        list = fcfs(int_list)
    elif radio_val == 1:
        list = sjf(int_list)
    elif radio_val == 2:
        list = priority(int_list)
    elif radio_val == 3:
        try:
            quanta = time_quanta.get()
        except TclError:
            error.set("Quanta is not a valid integer.")
            return

        if quanta <= 0:
            error.set("Quanta must be greater than 0")
            return
        list = rr(int_list, quanta)
    
    canvas.delete(ALL)
    run_time = 0
    for i in list:
        run_time += i[1]
        
    if run_time == 0:
        return
    
    spacing = 600/run_time
    canvas.create_rectangle(1, 1, 600, 50, fill='white')
    canvas.create_text(0, 50, anchor=NW, text=" 0")
    curr_time = 0
    index = 0
    for i in list:
        p_x_value = curr_time * spacing
        curr_time += i[1]
        x_value = curr_time * spacing
        canvas.create_line( x_value, 0, x_value, 50, fill='black')
        if index == len(list) - 1:
            canvas.create_text( x_value, 50, anchor=NE, text = curr_time)
        else:
            canvas.create_text( x_value, 50, anchor=N, text = curr_time)
        if i[0] != 0:
            canvas.create_text((p_x_value + x_value) / 2, 25, text = "P" + str(i[0]))
        index += 1
    return

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
    ttk.Label(q_frame, text="Time Quanta (RR only):").grid(row=0, column=0)
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
    
    can = Canvas(proc_sched, width=600, height=100)
    error = StringVar()

    #button setup
    b_frame = ttk.Frame(proc_sched)
    ttk.Button(b_frame, text="Add", command=lambda: add_process_row(s_frame)).grid(row=0, column=0)
    ttk.Button(b_frame, text="Clear", command=lambda: clear_process_row(s_frame)).grid(row=0, column=1)
    ttk.Button(b_frame, text="Run", command=lambda: parse_and_run_alg(radio_var.get(), quanta_var, can, error)).grid(row=0, column=2)
    b_frame.pack()
   
    ttk.Label(proc_sched, textvariable=error).pack()
    
    can.pack()
    
