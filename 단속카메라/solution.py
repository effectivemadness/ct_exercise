# def solution(routes):
#     answer = 0
#     routes.sort(key=lambda x:x[1])
#     pos = routes[0][0]
#     print(routes)
#     del_list = []
#     routes_len = len(routes)
#     while routes_len:
#         install = False
#         del_list = []
#         for i, item in enumerate(routes):
#             if item[0] == None:
#                 continue
#             elif item[1] == pos:
#                 install = True
#                 for j, item_j in enumerate(routes):
#                     if item_j[0] == None:
#                         continue
#                     elif item_j[0] <= pos and pos <= item_j[1]:
#                         del_list.append(j)
#         for i in sorted(del_list, reverse=True):
#             routes[i] = [None, None]
#             routes_len -= 1
#         if install:
#             answer += 1
#         pos+=1

#     return answer
##### 정확도 Pass, 효율성 Fail!

def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[1]) # routes를 차량이 나간 지점 (진출) 기준으로 정렬
    camera = -30001 # -30001부터 카메라 위치를 찾습니다.

    for route in routes:
        if camera < route[0]:
            answer += 1
            camera = route[1]
    return answer
print(solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]]))