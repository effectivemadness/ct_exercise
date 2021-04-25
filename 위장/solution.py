def solution(clothes):
    answer = 0
    clothes_dict = {}
    clothes_num = []
    for item in clothes:
        if clothes_dict.get(item[1]) is None:
            clothes_dict[item[1]] = 1
        else:
            clothes_dict[item[1]] += 1
    for item in clothes_dict:
        clothes_num.append(clothes_dict[item])
        if answer == 0:
            answer = clothes_dict[item] + 1
        else:
            answer = answer * (clothes_dict[item] + 1)
    return answer - 1

clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(clothes))