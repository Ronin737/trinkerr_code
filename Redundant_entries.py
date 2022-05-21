def redundant(entries,k):
    redun_map={}

    for ent in entries:
        if str(ent) in redun_map:
            redun_map[str(ent)]+=1
            continue
        redun_map[str(ent)]=1
    
    count=0
    highest_entries=[]
    while count!=k:
        highest_redun=0
        redun_ent=0
        for ent in redun_map:
            if redun_map[ent]>highest_redun:
                highest_redun=redun_map[ent]
                redun_ent=int(ent)
        
        highest_entries.append(redun_ent)
        count+=1
        redun_map.pop(str(redun_ent))
    
    return highest_entries

print(redundant([17, 17, 17, 18, 19, 16, 19, 19, 17],2))
        
