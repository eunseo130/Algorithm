def solution(lottos, win_nums):
    count = 0
    zero = 0
    for i in range(6):
        if lottos[i] == 0:
            zero += 1
    if zero != 6:
        for i in range(6):
            for j in range(6):
                if lottos[i] == win_nums[j]:
                    count += 1            
    answer = [0, 0]
    if zero + count == 6:
        answer[0] = 1
    elif zero + count == 5:
        answer[0] = 2
    elif zero + count == 4:
        answer[0] = 3
    elif zero + count == 3:
        answer[0] = 4
    elif zero + count == 2:
        answer[0] = 5
    elif zero + count <= 1:
        answer[0] = 6
     
    if count == 6:
        answer[0] = 1
        answer[1] = 1
    elif count == 5:
        answer[1] = 2
    elif count == 4:
        answer[1] = 3
    elif count == 3:
        answer[1] = 4
    elif count == 2:
        answer[1] = 5
    elif count <= 1:
        answer[1] = 6
        
    return answer