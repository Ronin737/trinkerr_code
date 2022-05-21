def lockup(cells, criminals):
    if len(cells)==1 and cells[0]==1:
        return False
    if len(cells)==2 and (cells[0]==1 or cells[1]==1):
        return False
    free_cells=0

    for i,cell in enumerate(cells):
        if cell==0:
            next_cell,prev_cell=i+1,i-1
            if i==0:
                if cells[next_cell]==0:
                    free_cells+=1
                    continue
            if i==len(cells)-1:
                if cells[prev_cell]==0:
                    free_cells+=1
                    continue
            if cells[next_cell]==0 and cells[prev_cell]==0:
                free_cells+=1
    
    if criminals>free_cells:
        return False
    
    return True


print(lockup([1,0,0,1],1))

