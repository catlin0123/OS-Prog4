from random import *
import copy

references = []

def setup_tables(tlb_size, num_pgs, num_fr):
    pg_ref = []
    fr_ref = []
    pg = []
    fr = [-1] * num_fr
    
    free = list(range(num_fr))
    for i in range(0, num_pgs):
        index = randint(0, len(free) - 1)
        pg.append(free[index])
        fr[free[index]] = i
        free.pop(index)
    
    free = list(range(num_pgs))
    x = min(tlb_size, num_pgs)
    for i in range(0, x):
        index = randint(0, len(free) - 1)
        pg_ref.append(free[index])
        fr_ref.append(pg[free[index]])
        free.pop(index)
    tlb = [pg_ref, fr_ref]
    
    return [tlb, pg, fr]

def run_tlb_manager(tlb, pg, fm):
    global references
 
    cur_pg = randint(0, len(pg) -1)
    references.append(cur_pg)
    
    if cur_pg in tlb[0]:
        return [1, tlb[0].index(cur_pg)]
    else:
        l = copy.copy(references)
        l.reverse()
        index_of_next_access = []
        for x in tlb[0]: 
            try:
                next = l.index(x)
                index_of_next_access.append(next)
            except:
                index_of_next_access.append(1000000000000000)
        return [0, cur_pg, index_of_next_access.index(max(index_of_next_access))]