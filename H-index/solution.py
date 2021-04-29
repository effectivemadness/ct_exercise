# def solution(citations):
#     answer = 0
#     max_ci = -1
#     print(sorted(citations))
#     citations = sorted(citations)
#     # for i, value in enumerate(citations):
#     #     if len(citations) - i >= value and max_ci < value:
#     #         max_ci = value
#     for i in range(len(citations)):
#         if len(citations) - i >= citations[i] and max_ci < citations[i]:
#             max_ci = citations[i]

#     return max_ci

def solution(citations):
    answer = 0
    citations.sort()
    cite_count = []
    for i in range(max(citations)+1):
        cite = 0
        for item in citations:
            if item >= i:
                cite = cite+1
            else:
                cite = cite+0
        cite_count.append(cite)
        # print(num)

        if cite_count[i] >= i:
            answer = i
        else:
            break

    return answer

print(solution([3, 0, 6, 1, 5]))
print(solution([1, 3, 5, 7, 9, 11]))