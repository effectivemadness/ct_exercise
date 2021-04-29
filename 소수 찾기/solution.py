from itertools import permutations 
def is_prime(number):
    if number < 2:
        return False
    elif number < 4:
        return True
    elif number % 2 == 0:
        return False
    # for i in range(5,number//2+1, 2):
    #     if number%i == 0:
    #         return False
    i = 3
    while True:
        if number % i == 0:
            return False
        if i * i >= number:
            return True
        i += 2
    return True
    
def solution(numbers):
    answer = 0
    number_list = []
    candiate_list = []
    for i in range(len(numbers)):
        number_list.append(numbers[i])
    for i in range(len(number_list)):
        number_perm = permutations(number_list, i+1)
        for item in number_perm:
            tmp_str = ""
            for num_str in item:
                tmp_str = tmp_str + str(num_str)
            if int(tmp_str) not in candiate_list:
                candiate_list.append(int(tmp_str))
    for item in candiate_list:
        if is_prime(item):
            answer += 1
    return answer

# for item in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 47, 53, 59, 67, 71, 83, 89, 101, 107, 109, 113, 127, 131, 137, 139, 149, 157, 167, 179, 181, 191, 197, 199, 211, 227, 233, 239, 251, 257, 263, 269, 281, 293, 307, 311, 317, 337, 347, 353, 359, 379, 389, 401, 409]:
#     if is_prime(item) is False:
#         print("False")
# print(is_prime(111))
print(solution("101010"))