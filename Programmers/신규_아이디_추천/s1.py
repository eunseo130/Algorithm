def solution(new_id):
    new_id = new_id.lower()
    for i in range(len(new_id)):
        if new_id[i].isalnum() == False:
            if new_id[i] not in ['-', '_', '.']:
                new_id = new_id.replace(new_id[i], " ")
    new_id = new_id.replace(" ", "")
    
    while ".." in new_id:
        new_id = new_id.replace('..', '.')
    
    new_id = new_id.strip('.')
    
    if new_id == "":
        new_id = 'a'
        
    if len(new_id)>=16:
        new_id = new_id[:15]
        
    new_id = new_id.rstrip('.')
    
    if len(new_id) <= 2:
        for k in range(3 - len(new_id)):
            new_id = new_id + new_id[-1]
    return new_id