
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
    return return_list

def sjf(processes):
    return_list = []
    current_time = 0
    while len(processes) != 0:
        #sort by arrival time first
        processes.sort(key=lambda x: x[3])
        i = 0
        if current_time < processes[i][3]:
            return_list.append([0, processes[i][3] - current_time])
            current_time += processes[i][3] - current_time
        while i < len(processes)and current_time >= processes[i][3]: 
            i += 1;
        sub_list = sorted(processes[0:i], key=lambda x: x[1])
        return_list.append([sub_list[0][0], sub_list[0][1]])
        current_time += sub_list[0][1]
        processes.remove(sub_list[0])
    return return_list

def priority(processes):
    return_list = []
    current_time = 0
    while len(processes) != 0:
        #sort by arrival time first
        processes.sort(key=lambda x: x[3])
        i = 0
        if current_time < processes[i][3]:
            return_list.append([0, processes[i][3] - current_time])
            current_time += processes[i][3] - current_time
        while i < len(processes)and current_time >= processes[i][3]: 
            i += 1;
        sub_list = sorted(processes[0:i], key=lambda x: x[2])
        return_list.append([sub_list[0][0], sub_list[0][1]])
        current_time += sub_list[0][1]
        processes.remove(sub_list[0])
    return return_list

def rr(processes, quanta):
    processes.sort(key=lambda x: x[3]) #sort by arrival time
    current_time = 0
    queue = []
    return_list = []
    app = []

    while len(processes) != 0 or len(queue) != 0 or len(app) != 0: 
        if len(processes) != 0 and current_time < processes[0][3] and len(queue) == 0:
            return_list.append([0, processes[0][3] - current_time])
            current_time += processes[0][3] - current_time
        
        while len(processes) != 0 and processes[0][3] <= current_time: 
            queue.append(processes[0])
            processes.pop(0)
        
        for x in app:
            queue.append(x)
        app = []
        
        if queue[0][1] <= quanta: 
            return_list.append([queue[0][0], queue[0][1]])
            current_time += queue[0][1]
            queue.pop(0)
        else:
            return_list.append([queue[0][0], quanta])
            current_time += quanta
            queue[0][1] -= quanta
            app.append(queue[0])
            queue.pop(0)
            
    return return_list
