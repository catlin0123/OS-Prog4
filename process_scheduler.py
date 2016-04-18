
def fcfs(processes):
    return_list = []
    processes.sort(key=lambda x: x[3]) #sort by arrival time
    current_time = 0
    for p in processes:
        if p[3] > current_time: 
            return_list.append([0, p[3] - current_time]) #process is currently idle
            current_time += p[3] - current_time
        return_list.append([p[0], p[1]])
        current_time += p[1]
    print (return_list)
    return

def sjf(processes):
    return_list = []
    processes.sort(key=lambda x: x[3]) #sort by burst time
    current_time = 0
    while (len(processes) > 0)
    {
    
    
    }
    return

def priority(processes):
    processes.sort(key=lambda x: x[2], reverse=True) #sort by priority
    print (processes)
    return

def rr(processes, quanta):
    processes.sort(key=lambda x: x[3]) #sort by arrival time
    print (processes)
    return
