# def solution(scoville, K):
#     answer = 0
#     sorted_scv = sorted(scoville)
#     while sorted_scv[0] < K:
#         answer += 1
#         if len(sorted_scv) == 1:
#             return -1
#         elif len(sorted_scv) == 2 and sorted_scv[0]+sorted_scv[1]*2 < K:
#             return -1
#         print(sorted_scv)
#         mixed = sorted_scv.pop(0) + sorted_scv.pop(0)*2
#         print(sorted_scv)
#         i = 0
#         while i < len(sorted_scv) and sorted_scv[i] < mixed:
#             i += 1
#         sorted_scv.insert(i, mixed)
#         print(sorted_scv)
#     return answer
import heapq
def solution(scoville, K):
    
    answer = 0
    heapq.heapify(scoville)
    print(scoville)
    while len(scoville) >= 2:
        answer += 1
        mixed = heapq.heappop(scoville) + heapq.heappop(scoville)*2
        heapq.heappush(scoville, mixed)
        if scoville[0] >= K:
            return answer
        print(scoville)
    if scoville[0] >= K:
        return answer
    else:
        return -1

print(solution([1, 2, 3, 9, 10, 12],7))
print(solution([8,8],7))