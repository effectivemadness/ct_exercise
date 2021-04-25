# def find_and_delete(item):
#     flag = 0
#     if item in part_arr[ord(item[0]) - ord('a')]:
#         flag = 1
#     part_arr[ord(item[0]) - ord('a')].remove(item)
#     return flag, item
# participant = ["leo", "kiki", "eden"]
# completion = ["eden", "kiki"]

people = {}

for item in participant:
    if people.get(item) is None:
        people[item] = 1
    else:
        people[item] += 1

for item in completion:
    if people.get(item) == 1:
        del people[item]
    elif people.get(item) > 1:
        people[item] -= 1
for p in people:
    answer = p
print(p)

# answer = ''
# part_arr = []
# for i in range(26*26):
#     part_arr.append([])

# for item in participant:
#     part_arr[(ord(item[0]) - ord('a'))*10+(ord(item[1]) - ord('a'))].append(item)
# # print(part_arr)
# for item in completion:
#     part_arr[(ord(item[0]) - ord('a'))*10+(ord(item[1]) - ord('a'))].remove(item)
# for item in part_arr:
#     if len(item) != 0:
#         answer = item
# print(answer)

# def solution(participant, completion):
#     answer = ''
#     part_arr = []
#     for i in range(26):
#         part_arr.append([])
#         for j in range(26):
#             part_arr[i].append([])

#     for item in participant:
#         part_arr[(ord(item[0]) - ord('a'))][(ord(item[1]) - ord('a'))].append(item)
#     # print(part_arr)
#     for item in completion:
#         part_arr[(ord(item[0]) - ord('a'))][(ord(item[1]) - ord('a'))].remove(item)
#     for i in range(26):
#         for j in range(26):
#             if len (part_arr[i][j]) != 0:
#                 answer = part_arr[i][j][0]
#     return answer