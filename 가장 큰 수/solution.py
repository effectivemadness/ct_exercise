# import itertools
# def solution(numbers):
#     answer = ''
#     str_list = itertools.permutations(numbers, len(numbers))
#     number_list = []
#     print(str_list)
#     for item in str_list:
#         tmp_str = ""
#         for num_str in item:
#             tmp_str = tmp_str + str(num_str)
#         number_list.append(int(tmp_str))
#     print(number_list)
#     return sorted(number_list)[-1]
#     # return answer

def solution(numbers):
    answer=""
    str_list=[]
    for i,num in enumerate(numbers):
        num_string = str(num)
        num_mult = num_string*3
        str_list.append([num_mult,i])
    print(str_list)
    str_list.sort(reverse=True)
    for i,value in enumerate(str_list):
        index = value[1]
        answer += str(numbers[index])


    for value in answer:
        if value!='0':
            return answer

    return "0"

print(solution([6, 10, 2]))