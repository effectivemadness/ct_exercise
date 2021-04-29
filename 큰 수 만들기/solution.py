# import itertools
# def solution(number, k):
#     answer = ''
#     number_list = []
#     str_list = itertools.combinations(number, len(number)-k)
#     # print(list(str_list))
#     for item in str_list:
#         tmp_str = ""
#         for num_str in item:
#             tmp_str = tmp_str + str(num_str)
#         number_list.append(int(tmp_str))
#     # print(number_list)
#     return sorted(number_list)[-1]
#     return answer
###### itertools timeout!!!

def solution(number, k):
    length = len(number) - k
    answer = []
    end_index = len(number) - (length-1)
    while len(answer) != length:
        temp = "0"
        for i in range(len(number[0:end_index])):
            if number[i] > temp:
                temp = number[i]
                char_index = i
                if number[i] == "9":
                    break
        if temp == "0":
            char_index = 0
        answer.append(temp)
        number = number[char_index+1:]
        end_index = len(number) - (length - 1 -len(answer))

    answer = ''.join(answer)
    return answer
print(solution("4177252841",4))