from random import *
import copy

def run_tlb_manager(pg, fm, mem, tlb):
    lookup = [0] * tlb
    return_list = []
    last_lookups = []
    
    #prefill the table to not end up with a large start up cost
    for i in range(0, tlb):
        lookup[i] = i
    
    for i in range(0, mem):
        cur_pg = next_pg(last_lookups, pg)
        last_lookups.append(cur_pg)
        
        if cur_pg in lookup:
            return_list.append(1)
        else:
            l = copy.copy(last_lookups[0:i])
            l.reverse()
            index_of_next_access = []
            for x in lookup: 
                try:
                    next = l.index(x)
                    index_of_next_access.append(next)
                except:
                    index_of_next_access.append(1000000000000000)
            index_to_change = index_of_next_access.index(max(index_of_next_access))
            lookup[index_to_change] = cur_pg
            return_list.append(0)
           
    
    return return_list
    
def next_pg (last, pg):
    is_local = randint(0, 4)
    if is_local == 0 or len(last) == 0: 
        return randint(0, pg)
    else:
        i =0
        if (len(last) < 20):
            i = len(last)
        else:
            i = 20
        x = randint(0, i -1)
        return last[-x]