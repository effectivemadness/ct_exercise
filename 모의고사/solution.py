def solution(answers):
    answer = []
    corr = []
    std1 = [1,2,3,4,5]
    std2 = [2, 1, 2, 3, 2, 4, 2, 5]
    std3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    corr_temp = 0
    for i in range(len(answers)):
        if std1[i%len(std1)] == answers[i]:
            corr_temp += 1
    corr.append(corr_temp)
    corr_temp = 0
    for i in range(len(answers)):
        if std2[i%len(std2)] == answers[i]:
            corr_temp += 1
    corr.append(corr_temp)
    corr_temp = 0
    for i in range(len(answers)):
        if std3[i%len(std3)] == answers[i]:
            corr_temp += 1
    corr.append(corr_temp)
    for i in range(len(corr)):
        if corr[i] == max(corr):
            answer.append(i+1)
    return answer

print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))