import copy

def fifo(list, num_frames):
    temp = fill(list, num_frames)
    return_list = temp[0]
    index = temp [1]
    index_to_change = 0
    for i in range(index, len(list)):
        curr = list[i]
        item = copy.copy(return_list[i -1])
        if curr in return_list[i - 1]:
            return_list.append(item)
        else: 
            item[index_to_change] = curr
            return_list.append(item)
            index_to_change += 1
            if index_to_change == num_frames:
                index_to_change = 0
    return return_list

def optimal(list, num_frames):
    temp = fill(list, num_frames)
    return_list = temp[0]
    index = temp [1]
    list = list[index: len(list)] 
    while (len(list) != 0):
        item = copy.copy(return_list[-1])
        curr = list[0]
        if curr in return_list[-1]:
            return_list.append(item)
        else: 
            index_of_next_access = []
            for i in item: 
                try:
                    next = list.index(i)
                    index_of_next_access.append(next)
                except:
                    index_of_next_access.append(1000000000000000)
            index_to_change = index_of_next_access.index(max(index_of_next_access))
            item[index_to_change] = curr
            return_list.append(item)
        list.pop(0)
    return return_list

def lru(list, num_frames):
    temp = fill(list, num_frames)
    return_list = temp[0]
    index = temp [1]
    for i in range(index, len(list)):
        curr = list[i]
        item = copy.copy(return_list[i -1])
        if curr in return_list[i - 1]:
            return_list.append(item)
        else: 
            l = copy.copy(list[0:i])
            l.reverse()
            index_of_next_access = []
            for i in item: 
                try:
                    next = l.index(i)
                    index_of_next_access.append(next)
                except:
                    index_of_next_access.append(1000000000000000)
            index_to_change = index_of_next_access.index(max(index_of_next_access))
            item[index_to_change] = curr
            return_list.append(item)
    return return_list

def lfu(list, num_frames, num_pages):
    ref_count = [0] * num_pages; 
    temp = fill(list, num_frames)
    return_list = temp[0]
    index = temp [1]
    for i in range(0, index): 
        ref_count[list[i]] += 1
    for i in range(index, len(list)): 
        curr = list[i]
        ref_count[curr] += 1
        item = copy.copy(return_list[i -1])
        if curr in return_list[i - 1]:
            return_list.append(item)
        else: 
            count_array = []
            for i in item: 
                count = ref_count[i]
                count_array.append(count)
            index_to_change = count_array.index(min(count_array))
            item[index_to_change] = curr
            return_list.append(item)
    return return_list

def nru(list, acc, num_frames, num_pages, ref_update): 
    num_ref = 0
    index = 0
    
    space_in_list = num_frames
    ref_list = [0] * num_pages
    mod_list = [0] * num_pages
    return_list = []
    
    #fill the frames no collisions will occur
    while space_in_list != 0 and len(list) != len(return_list):
        if (index % ref_update) == 0: #time to update the list
            ref_list = [0] * num_pages
        if space_in_list == num_frames:
            if acc[0] == 1:
                mod_list[list[0]] += 1
            ref_list[list[0]] += 1
            l = [-1] * num_frames
            l[0] = list[0]
            return_list.append(l)
            space_in_list -=1
        else:
            item = copy.copy(return_list[index - 1])
            if acc[index] == 1:
                mod_list[list[index]] += 1
            ref_list[list[index]] += 1
            if list[index] in return_list[index - 1]:
                return_list.append(item)
            else :
                i = item.index(-1); 
                item[i] = list[index]
                return_list.append(item)
                space_in_list -=1
        index += 1
    
    #figure out if you have a collision and do stuff about it
    for i in range(index, len(list)):
        if i % ref_update == 0: #time to update the list
            ref_list = [0] * num_pages
            
        curr = list[i]
        item = copy.copy(return_list[i -1])
        if curr in return_list[i - 1]:
            return_list.append(item)
        else: 
            l = sorted(item, key=lambda x: mysort(ref_list, mod_list, x))
            ref_list[l[0]] = 0
            mod_list[l[0]] = 0
            index_change = item.index(l[0])
            item[index_change] = curr
            return_list.append(item)
        if acc[i] == 1:
            mod_list[list[i]] += 1
        ref_list[list[i]] += 1
     
    return return_list
    
def fill(list, num_frames):
    return_list = []
    space_in_list = num_frames
    index = 0;
    while space_in_list != 0 and len(list) != len(return_list):
        if space_in_list == num_frames:
            l = [-1] * num_frames
            l[0] = list[0]
            return_list.append(l)
            space_in_list -=1
        else:
            item = copy.copy(return_list[index - 1])
            if list[index] in return_list[index - 1]:
                return_list.append(item)
            else :
                i = item.index(-1); 
                item[i] = list[index]
                return_list.append(item)
                space_in_list -=1
        index += 1
    return (return_list, index)

def mysort(ref_list, mod_list, x):
    if ref_list[x] != 0 and mod_list[x] != 0:
        return 3
    if ref_list[x] != 0 and mod_list[x] == 0:
        return 2
    if ref_list[x] == 0 and mod_list[x] != 0:
        return 1
    if ref_list[x] == 0 and mod_list[x] == 0:
        return 0