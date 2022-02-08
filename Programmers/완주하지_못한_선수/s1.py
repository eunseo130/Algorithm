def solution(participant, completion):
    for i in range(len(completion)):
        if completion[i] in participant:
            participant.remove(completion[i])
    answer = ''
    answer = participant[0]
    return answer