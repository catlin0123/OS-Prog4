import copy

def fifo(list, num_frames):
    temp = fill(list, num_frames)
    return_list = temp[0]
    index = temp [1]
    index_to_change = 0
    num_changes = 0
    for i in range(index, len(list)):
        curr = list[i]
        item = copy.copy(return_list[i -1])
        if curr in return_list[i - 1]:
            return_list.append(item)
        else: 
            num_changes += 1
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
    num_changes = 0
    while (len(list) != 0):
        item = copy.copy(return_list[-1])
        curr = list[0]
        if curr in return_list[-1]:
            return_list.append(item)
        else: 
            num_changes += 1
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
    num_changes = 0
    for i in range(index, len(list)):
        curr = list[i]
        item = copy.copy(return_list[i -1])
        if curr in return_list[i - 1]:
            return_list.append(item)
        else: 
            num_changes += 1
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
    num_changes = 0
    for i in range(0, index): 
        ref_count[list[i]] += 1
    for i in range(index, len(list)): 
        curr = list[i]
        ref_count[curr] += 1
        item = copy.copy(return_list[i -1])
        if curr in return_list[i - 1]:
            return_list.append(item)
        else: 
            num_changes += 1
            count_array = []
            for i in item: 
                count = ref_count[i]
                count_array.append(count)
            index_to_change = count_array.index(min(count_array))
            item[index_to_change] = curr
            return_list.append(item)
    return return_list

def nru(list, num_frames, ref_update): 
    temp = fill(list, num_frames)
    return_list = temp[0]
    index = temp [1]
    return return_list
    
def fill(list, num_frames):
    return_list = []
    space_in_list = num_frames
    index = 0;
    while space_in_list != 0:
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
