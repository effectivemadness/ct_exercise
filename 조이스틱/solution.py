# def get_diff(name_fix,name, curr):
#     for i in range(len(name)):
#         if name[abs((curr-i) % len(name))] != '0' and name[abs((curr-i) % len(name))] != 'A':
#             print(abs(curr-i))
#             return abs((curr-i))
#         elif name[abs((curr+i) % len(name))] != '0' and name[abs((curr+i) % len(name))] != 'A':
#             print(abs((curr+i) % len(name)))
#             return abs((curr+i) % len(name))

# def solution(name):
#     answer = 0
#     cur = 0
#     name_fix = ""
#     for i in name:
#         name_fix += i
#     for i in range(len(name)):
#         # print(ord(i)-ord('A'))
#         if abs(1 - (ord(name[cur]) - ord('A'))) < abs((ord('A') - ord(name[cur]) - 1)):
#             answer += abs((ord(name[cur]) - ord('A')))
#             name = list(name)
#             name[cur] = '0'
#             name = "".join(name)
#         elif abs(1 - (ord(name[cur]) - ord('A'))) > abs((ord('A') - ord(name[cur]) - 1)):
#             answer += abs((ord('A') - ord(name[cur])))
#             name = list(name)
#             name[cur] = '0'
#             name = "".join(name)
#         # print(get_diff(name_fix, name, cur))
        
#         if get_diff(name_fix, name, cur) is None:
#             break
#         diff =abs(cur - get_diff(name_fix, name, cur))
#         answer += abs(cur - diff)
#         cur = diff
#         # answer+=1
#     return answer - 1

def solution(name):


    import itertools
    indexes = [ i for i, c in enumerate(name) if c != 'A' ]
    print(indexes)
    # dictionary for distances
    d_distance = {}
    for i in set([0]+indexes):
        for j in set([0]+indexes):
            d_distance[f"{i}_{j}"] = min([(len(name)-i+j)%len(name), (len(name)+i-j)%len(name)])
    print(d_distance)
    # dictionary for switching costs 
    d_switch = {}
    for i in set([name[i] for i in indexes]):
        d_switch[i] = min(ord(i)-ord('A'), 26+ord('A')-ord(i))

    answer = float('inf')
    res_switch = sum([d_switch[name[i]] for i in indexes])
    for case in itertools.permutations(indexes):
        res = res_switch
        start = 0
        for i in case:
            res = res + d_distance[f"{start}_{i}"]
            start = i
        answer = min(answer, res)
    return answer
print(solution("ABZ"))