# def get_max(priorities):
#     max = -1
#     for i in range(1, len(priorities)):

def solution(priorities, location):
    answer = 0
    
    while True:
        if len(priorities) == 1:
            return answer + 1
        while priorities[0] < max(priorities[1:]):
            priorities.append(priorities.pop(0))
            
            if not location:
                location = len(priorities) - 1
            else:
                location -= 1
        if location == 0:
            break
        else :
            answer += 1
            priorities.pop(0)
            location -=1
        print(priorities, location)
    return answer + 1

print(solution([2, 1, 3, 2],2))
print(solution([1, 1, 9, 1, 1, 1],1))