from tkinter import *
from tkinter import ttk
from mem_management import *

def run_alg(page_var, frame_var, mem_acc_var, tlb_size, disp_frame):
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
    
    disp_frame = ttk.Frame(mem_man)
   
    ttk.Button(mem_man, text="Run", command=lambda: run_alg(page_var, frame_var, mem_acc_var, tlb_size, disp_frame)).pack()
        
    disp_frame.pack()