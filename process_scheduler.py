
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
    return return_list

def sjf(processes):
    return_list = []
    processes.sort(key=lambda x: x[3]) #sort by arrival time first if they aren't there we can't do it.
    current_time = 0
    i = 0
    #while processes.len() != 0:    
    return return_list

def priority(processes):
    return_list = []
    processes.sort(key=lambda x: x[3]) #sort by arrival time first. 
    print (processes)
    return return_list

def rr(processes, quanta):
    processes.sort(key=lambda x: x[3]) #sort by arrival time
    return_list = []
    current_time = 0
    i = 0
    while len(processes) != 0: 
        if current_time < processes[i][3]:
            return_list.append([0, processes[i][3] - current_time])
            current_time += processes[i][3] - current_time
        if processes[i][1] <= quanta: 
            return_list.append([processes[i][0], processes[i][1]])
            current_time += processes[i][1]
            processes.pop(i)
        else:
            return_list.append([processes[i][0], quanta])
            current_time += quanta
            processes[i][1] -= quanta
            i += 1
        if i >= len(processes):
            i = 0;     
        
    print (return_list)
    return return_list
