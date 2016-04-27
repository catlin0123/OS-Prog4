from tkinter import *
from tkinter import ttk
from mem_management import *

def run_alg(page_var, frame_var, mem_acc_var, tlb_size, error, canvas):
    error.set("")
    try:
        pg = page_var.get()
        fm = frame_var.get()
        mem = mem_acc_var.get()
        tlb = tlb_size.get()
    except TclError:
        error.set("All parameters must be integers.")
        return
    
    if pg <= 0 or fm <= 0 or mem <= 0 or tlb <= 0: 
        error.set("All values must be greater than 0")
        return 
        
    list = run_tlb_manager(pg, fm, mem, tlb)
    
    canvas.delete(ALL)
    spacing = 600/mem
    index = 0
    hit_count = 0 
    miss_count = 0
    for i in list:
        x_value = index * spacing
        if i == 0:
            canvas.create_rectangle(x_value, 0, x_value + spacing, 50, fill='red', outline='red')
            miss_count += 1
        else:
            canvas.create_rectangle(x_value, 0, x_value + spacing, 50, fill='green', outline='green')
            hit_count += 1
        index += 1
    hit_ratio = hit_count / (hit_count + miss_count)
    miss_ratio = 1 - hit_ratio
    mess = "Hit Count: " + str(hit_count) + "\nMiss Count: " + str(miss_count)
    mess += "\nHit Ratio: " + str(hit_ratio) + "\nMiss Ratio: " + str(miss_ratio)
    error.set(mess)
    return
        
def create_mem_management_view(mem_man):

    q_frame = ttk.Frame(mem_man)
    ttk.Label(q_frame, text="Number of pages:").grid(row=0, column=0)
    page_var = IntVar()
    ttk.Entry(q_frame, textvariable=page_var).grid(row=0, column=1)
    
    ttk.Label(q_frame, text="Number of frames:").grid(row=1, column=0)
    frame_var = IntVar()
    ttk.Entry(q_frame, textvariable=frame_var).grid(row=1, column=1)
    
    ttk.Label(q_frame, text="Number of memory acesses:").grid(row=2, column=0)
    mem_acc_var = IntVar()
    ttk.Entry(q_frame, textvariable=mem_acc_var).grid(row=2, column=1)
    q_frame.pack()
    
    ttk.Label(q_frame, text="TLB Size:").grid(row=3, column=0)
    tlb_size = IntVar()
    ttk.Entry(q_frame, textvariable=tlb_size).grid(row=3, column=1)
    q_frame.pack()
    
    can = Canvas(mem_man, width=600, height=100)
    error = StringVar()
   
    ttk.Button(mem_man, text="Run", command=lambda: run_alg(page_var, frame_var, mem_acc_var, tlb_size, error, can)).pack()
    
    ttk.Label(mem_man, textvariable=error).pack()
    can.pack()