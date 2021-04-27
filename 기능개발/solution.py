def solution(progresses, speeds):
    answer = []
    days = 0
    while True:
        daily_done = 0
        for i in range(len(progresses)):
            progresses[i] = progresses[i] + speeds[i]
        print(progresses)
        while True:
            if len(progresses) and  progresses[0] >= 100:
                progresses.pop(0)
                speeds.pop(0)
                daily_done += 1
            else : 
                break
        if daily_done:
            answer.append(daily_done)
        if len(progresses) == 0:
            break
    # print(progresses*)
    return answer

print(solution([93, 30, 55],[1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1]))
print(solution([95, 1],[1, 7]))