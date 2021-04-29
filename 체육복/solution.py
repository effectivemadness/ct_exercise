def solution(n, lost, reserve):
    for i in range(len(reserve)):
        if reserve[i] in lost:
            lost[lost.index(reserve[i])] = -1
            reserve[i] = -1
    lost_num = 0
    for i in lost:
        if i != -1:
            lost_num += 1
    std = n - lost_num
    for i in lost:
        if i != -1:
            if i-1 in reserve:
                reserve.remove(i-1)
                std += 1
            elif i+1 in reserve:
                reserve.remove(i+1)
                std += 1
    
    return std


print(solution(5,[2, 4, 3],[1, 3, 5]))
print(solution(7, [2,4,5,6,7], [1,3,4,5,6,7]))