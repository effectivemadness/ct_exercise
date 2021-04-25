# def solution(bridge_length, weight, truck_weights):
#     answer = 0
#     e_time = -1
#     on_weight = 0
#     pass_cnt = 0
#     bridge = []
#     while True:
#         print(len(bridge), on_weight, truck_weights)
#         e_time += 1
#         if len(bridge) == 0 and len(truck_weights) == 0:
#             break
#         if len(bridge) != 0:
#             last_weight = bridge.pop()
#             if pass_cnt < bridge_length:
#                 pass_cnt += 1
#             if len(bridge) == 0 or pass_cnt == bridge_length:
#                 on_weight -= last_weight
#                 pass_cnt = 0
#         if len(truck_weights) != 0 and weight - on_weight >= truck_weights[0]:
#             for i in range(bridge_length):
#                 bridge.append(truck_weights[0])
#             on_weight += truck_weights[0]
#             truck_weights.pop(0)
#     answer = e_time - 1
#     return answer

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = []
    on_weight = 0
    intime = 1
    i = 0
    while i < len(truck_weights):
        if (on_weight + truck_weights[i] <= weight):
            bridge.append((truck_weights[i], intime, intime+bridge_length))
            on_weight += truck_weights[i]
            intime += 1
            i += 1
        else :
            on_weight -= bridge[0][0]
            if (intime > bridge[0][2]):
                intime = intime
            else:
                intime = bridge[0][2] 
            bridge.pop(0)
        print(bridge)
    print(bridge[-1])
    return answer

print(solution(2, 10, [7,4,5,6]))
print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))
print(solution(5, 5, [2, 2, 2, 2, 1, 1, 1, 1, 1]	))