def solution(array, commands):
    answer = []
    for item in commands:
        temp_list = array[item[0]-1:item[1]]
        temp_list = sorted(temp_list)
        answer.append(temp_list[item[2]-1])
    return answer

print(solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]]))