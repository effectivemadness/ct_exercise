def solution(phone_book):
    answer = True
    phone_dict = {}
    phone_book=sorted(phone_book, key=len, reverse=True)
    print(phone_book)
    for item in phone_book:
        for i in range(len(item)):
            if phone_dict.get(item[:i+1]) is None:
                phone_dict[item[:i+1]] = item
            else:
                answer = False
    return answer

phone_book = ["119", "97674223", "1195524421"]

print(solution(phone_book))