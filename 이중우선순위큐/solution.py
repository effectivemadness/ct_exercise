import heapq
def add_item(min_heap, max_heap, item):
    heapq.heappush(min_heap, item)
    heapq.heappush(max_heap, (-item, item))
def del_max(min_heap, max_heap):
    if len(min_heap) == 0:
        return
    max_val = heapq.heappop(max_heap)[1]
    min_heap.remove(max_val)
    heapq.heapify(min_heap)
def del_min(min_heap, max_heap):
    if len(min_heap) == 0:
        return
    min_val = heapq.heappop(min_heap)
    max_heap.remove((-min_val, min_val))
    heapq.heapify(max_heap)
def get_minmax(min_heap, max_heap):
    if len(min_heap) == 0:
        return [0, 0]
    elif len(min_heap) == 1:
        return [1, 1]
    else :
        return [max_heap[0][1],min_heap[0]]
def solution(operations):
    answer = []
    max_heap = []
    min_heap = []
    for i in operations:
        if i[0] == 'I':
            add_item(min_heap,max_heap, int(i[2:]))
        elif i == "D 1":
            del_max(min_heap, max_heap)
        elif i == "D -1":
            del_min(min_heap, max_heap)
    return get_minmax(min_heap, max_heap)

print(solution(["I 16","D 1"]))

