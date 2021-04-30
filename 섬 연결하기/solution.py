# def solution(n, costs):
#     answer = 0
#     costs.sort(key=lambda x:x[2])
#     connected = set([1])
#     not_connected = set([i for i in range(1,n)])
#     cost_clean = []
#     if n == 1:
#         return 0
#     for item in costs:
#         cost_clean.append([[item[0],item[1]], item[2]])
#     while len(not_connected):
#         min_cost = 9999999999999 
#         min_index = None
#         for i,item in enumerate(cost_clean):
#             #check if both node in set
#             if item[0][0] in connected and item[0][1] in connected:
#                 item[1] = -1
#             #minimum cost connecting outside
#             if (item[0][0] in connected or item[0][1] in connected) and item[1] != -1:
#                 if min_cost>item[1]:
#                     min_cost = item[1]
#                     min_index = i
#         #add node to connected, delete vertex
#         answer+=cost_clean[min_index][1]
#         for i in cost_clean[min_index][0]:
#             connected.add(i)
#             if i in not_connected:
#                 not_connected.remove(i)
#     return answer
#### 1,8번 테스트 통과 X -> 이유 못찾겠음

def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x: x[2])
    visited = [0] * n
    visited[0] = 1 #임의의 하나 일단 1로 둠. =visit함 
    while sum(visited) != n:
        for cost in costs:
            s, e, c = cost #start, end, cost
            if visited[s] or visited[e]: #start, end 둘 중 하나 1이면 
                if visited[s] and visited[e]: #그 중에서도 start, end 둘다 1이면 
                    continue #둘이 연결되었다는 거니까 그냥 넘어감.
                else: #둘중 하나만 1이면 
                    visited[s] = 1 #둘다 visit됨 처리. 
                    visited[e] = 1
                    answer += c #answer 
                    break
    return answer

print(solution(5, [[0, 1, 5], [1, 2, 3], [2, 3, 3], [3, 1, 2], [3, 0, 4], [2, 4, 6], [4, 0, 7]])," sol: ", 15)
print(solution(5, [[0, 1, 1], [3, 4, 1], [1, 2, 2], [2, 3, 4]])," sol: ", 8)
print(solution(4, [[0, 1, 5], [1, 2, 3], [2, 3, 3], [1, 3, 2], [0, 3, 4]])," sol: ", 9)
print(solution(5, [[0, 1, 1], [3, 1, 1], [0, 2, 2], [0, 3, 2], [0, 4, 100]])," sol: ", 104)
print(solution(6, [[0, 1, 5], [0, 3, 2], [0, 4, 3], [1, 4, 1], [3, 4, 10], [1, 2, 2], [2, 5, 3], [4, 5, 4]])," sol: ", 11)
print(solution(5, [[0, 1, 1], [2, 3, 1], [3, 4, 2], [1, 2, 2], [0, 4, 100]])," sol: ", 6)
print(solution(5, [[0, 1, 1], [0, 4, 5], [2, 4, 1], [2, 3, 1], [3, 4, 1]])," sol: ", 8)
print(solution(5, [[0, 1, 1], [0, 2, 2], [0, 3, 3], [0, 4, 4], [1, 3, 1]])," sol: ", 8)
print(solution(6, [[0, 1, 5], [0, 3, 2], [0, 4, 3], [1, 4, 1], [3, 4, 10], [1, 2, 2], [2, 5, 3], [4, 5, 4]]), "sol: ", 11)