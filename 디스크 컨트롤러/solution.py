import heapq
def solution(jobs):
    answer = 0
    # dict_list = dict(jobs)
    # di = list(dict_list.items())
    # print(di)
    heapq.heapify(jobs)
    added_queue = []
    print(jobs)
    job_count = len(jobs)
    # for i in range(len(jobs)):
    #     print(heapq.heappop(jobs))
    time = 0
    working = False
    curr_work = None
    time_sum = 0
    while True:
        while len(jobs):
            if jobs[0][0] == time:
                temp_job = heapq.heappop(jobs)
                heapq.heappush(added_queue,[temp_job[1],temp_job[0]])
            else :
                break
        print("---time--- : ", time)
        print("jobs:",jobs)
        print("queue : ",added_queue)
        if curr_work is not None and curr_work[0] == time - start_time:
            working = False
            time_sum += time - curr_work[1]
        if not working and len(added_queue):
            curr_work = heapq.heappop(added_queue)
            working = True
            start_time = time
        elif not working and len(jobs) == 0 :
            break
        time += 1
        
            
    return time_sum // job_count

print(solution([[0, 3], [1, 9],[12,5], [2, 6],[4,24], [6,12]]))
print(solution([[0, 3], [1, 9], [2, 6]]))