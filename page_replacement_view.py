from tkinter import *
from tkinter import ttk
from page_replacement import *
from random import *



def run_alg(alg, page, frame, mem, ref_clear, disp_frame, error):
    error.set("")
    try:
        num_ref = mem.get()
        pg = page.get()
        fr = frame.get()
    except TclError:
        error.set("All values must be integers.")
        return
        
    if num_ref <= 0 or pg <= 0 or fr <= 0:
        error.set("All values must be greater 0")
        return

    for w in disp_frame.winfo_children():
        w.destroy()
    ttk.Label(disp_frame, text = "Reference String:").grid(row = 0, column = 0)
    num_ref = mem.get()
    list = []
    ref_str = ""; 
    for i in range(0, num_ref):
        ref_to = randint(0, pg - 1)
        list.append(ref_to)
        ttk.Label(disp_frame, text = str(ref_to)).grid(row = 0, column = i + 1)
    
    disp_list = []
    
    row_val = 1
    if alg == 0: 
        dis_list = fifo(list, fr)
    elif alg == 1: 
        dis_list = optimal(list, fr)
    elif alg == 2:
        dis_list = lru(list, fr)
    elif alg == 3:
        dis_list = lfu(list, fr, pg)
    else: 
        rw = []
        for i in range(0, num_ref):
            ref_to = randint(0, 1)
            rw.append(ref_to)
            s = ""
            if ref_to == 0: 
                s = "r"
            else:
                s = "w"
            ttk.Label(disp_frame, text = s).grid(row = 1, column = i + 1)
        row_val +=1
        try:
            rc = ref_clear.get()
        except TclError:
            error.set("All values must be integers.")
            return
        if rc <= 0:
            error.set("All values must be greater than 0")
            return
        dis_list =  nru(list, rw, fr, pg, rc)
       
    ttk.Label(disp_frame, text = "Frames:").grid(row = row_val, column = 0)
    col = 1
    for column in dis_list:
        row = row_val
        for cell in column:
            if (cell != -1):
                ttk.Label(disp_frame, text=cell).grid(row =row, column=col)
            row += 1
        col += 1
    disp_frame.pack()
    return

def create_page_replacement_view(page_repl):
    radio_var = IntVar()
    ttk.Label(page_repl, text="Algoritm:").pack(anchor = W)

    #algorithm type setup
    ttk.Radiobutton(page_repl, text="First In First Out", variable=radio_var, value=0).pack(anchor = W)
    ttk.Radiobutton(page_repl, text="Optimal", variable=radio_var, value=1).pack(anchor = W)
    ttk.Radiobutton(page_repl, text="Least Recently Used", variable=radio_var, value=2).pack(anchor = W)
    ttk.Radiobutton(page_repl, text="Least Frequently Used", variable=radio_var, value=3).pack(anchor = W)
    ttk.Radiobutton(page_repl, text="Not Recently Used", variable=radio_var, value=4).pack(anchor = W)

    #time quantum setup
    q_frame = ttk.Frame(page_repl)
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
    
    ttk.Label(q_frame, text="References between clears (NRU only)").grid(row=3, column=0)
    ref_clear = IntVar()
    ttk.Entry(q_frame, textvariable=ref_clear).grid(row=3, column=1)
    q_frame.pack()
    
    disp_frame = ttk.Frame(page_repl)
    error = StringVar()
   
    ttk.Button(page_repl, text="Run", command=lambda: run_alg(radio_var.get(), page_var, frame_var, mem_acc_var, ref_clear, disp_frame, error)).pack()
        
    ttk.Label(page_repl, textvariable=error).pack()
    disp_frame.pack()
    
    