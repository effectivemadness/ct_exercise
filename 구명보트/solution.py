# def solution(people, limit):
#     answer = 0
    
#     while len(people) != 0:
#         boat_weight = 0
#         del_list = []
#         for i in range(len(people)):
#             if boat_weight + people[i] <= limit:
#                 boat_weight += people[i]
#                 del_list.append(i)
#         for i in sorted(del_list, reverse=True):
#             del people[i]
#         answer += 1
#     return answer

def solution(people, limit):
    answer = 0
    people.sort()
    left = 0
    right = len(people) - 1
    while left < right:
        if people[left] + people[right] <= limit:
            left += 1
            right -= 1
        else:
            right -= 1
        answer += 1
    if left == right:
        answer += 1

    return answer

print(solution([70, 50, 80, 50],100))