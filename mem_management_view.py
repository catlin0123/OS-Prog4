from tkinter import *
from tkinter import ttk
from mem_management import *

tables = []
hit_count = 0
miss_count = 0

def display_tables(tlb_frame, pt_frame, ft_frame, disp_frame, hit, ind, tlb_index):
    global tables
    fr = 0
    
    for w in tlb_frame.winfo_children():
        w.destroy()
    for w in pt_frame.winfo_children():
        w.destroy()
    for w in ft_frame.winfo_children():
        w.destroy()
    
    
    #display tlb
    ttk.Label(tlb_frame, text="Page number").grid(row = 0, column = 0)
    ttk.Label(tlb_frame, text="Frame number").grid(row = 0, column = 1)
    index = 0
    for i in tables[0][0]:
        if hit == 1 and index == ind:
            ttk.Label(tlb_frame, text=i, background="green").grid(row = index + 1, column = 0)
        elif hit == 0 and index == tlb_index:
            ttk.Label(tlb_frame, text=i, background="yellow").grid(row = index + 1, column = 0)
        else: 
            ttk.Label(tlb_frame, text=i).grid(row = index + 1, column = 0)
        index += 1
    
    index = 0
    for i in tables[0][1]:
        if hit == 1 and index == ind:
            fr = i
            ttk.Label(tlb_frame, text=i, background="green").grid(row = index + 1, column = 1)
        elif hit == 0 and index == tlb_index:
            fr = i
            ttk.Label(tlb_frame, text=i, background="yellow").grid(row = index + 1, column = 1)
        else: 
            ttk.Label(tlb_frame, text=i).grid(row = index + 1, column = 1)
        index += 1
        
    tlb_frame.grid(row = 1, column=0, sticky=W +E)
    
    #display page table
    ttk.Label(pt_frame, text="Index").grid(row = 0, column = 0)
    ttk.Label(pt_frame, text="Frame number").grid(row =0, column = 1)
    index = 0
    for i in tables[1]:
        if hit == 0 and ind == index:
            ttk.Label(pt_frame, text=str(index), background="red").grid(row = index+1, column = 0)
            ttk.Label(pt_frame, text=i, background="red").grid(row=index+1, column=1)
        else: 
            ttk.Label(pt_frame, text=str(index)).grid(row = index+1, column = 0)
            ttk.Label(pt_frame, text=i).grid(row=index+1, column=1)
        index += 1
    pt_frame.grid(row=1, column=1, sticky=W +E)
    
    #display frame tables
    ttk.Label(ft_frame, text="Index").grid(row = 0, column = 0)
    ttk.Label(ft_frame, text="Page Correlation").grid(row = 0, column = 1)
    index = 0
    for i in tables[2]:
        if hit != -1 and index == fr: 
            ttk.Label(ft_frame, text=str(index), background="green").grid(row = index +1, column = 0)
            ttk.Label(ft_frame, text=i, background="green").grid(row = index + 1, column = 1)
        else:
            ttk.Label(ft_frame, text=str(index)).grid(row = index +1, column = 0)
            ttk.Label(ft_frame, text=i).grid(row = index + 1, column = 1)
        index += 1
    ft_frame.grid(row=1, column=2, sticky=W +E)
        
    disp_frame.pack(fill=BOTH, expand=1)

def setup(page_var, frame_var, tlb_size, error, tlb_frame, pt_frame, ft_frame, disp_frame):
    global tables
    error.set("")
    try:
        pg = page_var.get()
        fm = frame_var.get()
        tlb = tlb_size.get()
    except TclError:
        error.set("All parameters must be integers.")
        return
    
    if pg <= 0 or fm <= 0 or tlb <= 0: 
        error.set("All values must be greater than 0")
        return 
        
    if pg > fm: 
        error.set("The number of frames must be greater than the number of pages.")
        return
        
    tables = setup_tables(tlb, pg, fm)
    display_tables(tlb_frame, pt_frame, ft_frame, disp_frame, -1, -1, -1)

def run_alg(error, tlb_frame, pt_frame, ft_frame, disp_frame):
    global tables
    global hit_count
    global miss_count
    pg = -1   
    list = run_tlb_manager(tables[0], tables[1], tables[2])
    
    #miss
    if list[0] == 0: 
        miss_count += 1
        pg = list[1]
        fm = tables[1][list[1]]
        tables[0][0][list[2]] = pg
        tables[0][1][list[2]] = fm
        display_tables(tlb_frame, pt_frame, ft_frame, disp_frame, list[0], list[1], list[2])
    #hit
    else: 
        hit_count += 1
        pg = tables[0][0][list[1]]
        display_tables(tlb_frame, pt_frame, ft_frame, disp_frame, list[0], list[1], -1)
       
    hit_ratio = hit_count / (hit_count + miss_count)
    miss_ratio = 1 - hit_ratio
    mess = "Page referenced:" + str(pg)
    mess += "\nHit Count: " + str(hit_count)
    mess += "\nMiss Count: " + str(miss_count)
    mess += "\nHit Ratio: " + str(hit_ratio) 
    mess += "\nMiss Ratio: " + str(miss_ratio)
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
    
    ttk.Label(q_frame, text="TLB Size:").grid(row=3, column=0)
    tlb_size = IntVar()
    ttk.Entry(q_frame, textvariable=tlb_size).grid(row=3, column=1)
    q_frame.pack()
    
    disp_frame = ttk.Frame(mem_man)
    ttk.Label(disp_frame, text="TLB", width = 50).grid(row=0, column=0)
    ttk.Label(disp_frame, text="Page Table", width = 50).grid(row=0, column=1)
    ttk.Label(disp_frame, text="Frame Table", width=50).grid(row=0, column=2)
    
    tlb_frame = ttk.Frame(disp_frame)
    tlb_frame.grid(column=0, row=1, sticky=W +E)
    
    pt_frame = ttk.Frame(disp_frame)
    pt_frame.grid(column=1, row=1, sticky=W +E)
    
    ft_frame = ttk.Frame(disp_frame)
    ft_frame.grid(column=2, row=1, sticky=W +E)
    
    error = StringVar()
   
    ttk.Button(mem_man, text="Setup", command=lambda: setup(page_var, frame_var, tlb_size, error, tlb_frame, pt_frame, ft_frame, disp_frame)).pack()
    ttk.Button(mem_man, text="Next", command=lambda: run_alg(error, tlb_frame, pt_frame, ft_frame, disp_frame)).pack()
    
    ttk.Label(mem_man, textvariable=error).pack()
    disp_frame.pack(fill=BOTH, expand=1)