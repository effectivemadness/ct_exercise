def solution(genres, plays):
    answer = []
    genre_dict = {}

    index = 0
    
    for item in zip(genres, plays):
        if genre_dict.get(item[0]) is None:
            genre_dict[item[0]] = {0 : index}
            index += 1
        else:
            genre_dict[item[0]][len(genre_dict[item[0]])] = index
            index += 1
    # for item in genre_dict:
        # print(genre_dict[item].values())
        # print(sum(genre_dict[item].values()[0]))
    
    # print(genre_dict)
        
    sorted_genre = sorted(genre_dict.items(), key=(lambda x: sum(map(lambda y : plays[y], x[1].values()))), reverse=True)
    # print(sorted_genre)
    for item in sorted_genre:
        sorted_plays = sorted(item[1].items(), key=(lambda x: plays[x[1]]),reverse=True)
        answer.append(sorted_plays[0][1])
        if len(sorted_plays) > 1:
            answer.append(sorted_plays[1][1])
        # print(sorted_plays)
    # print(genre_dict)
    return answer

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
print(solution(genres, plays))
print(solution(['A', 'B', 'A', 'A', 'B'], [
      500, 600, 150, 800, 2500]) == [4, 1, 3, 0])
print(solution(['B', 'A'], [500, 600]) == [1, 0])
print(solution(['B'], [500]) == [0])
print(solution(['B', 'A'], [600, 500]) == [0, 1])
print(solution(['A', 'B'], [600, 500]) == [0, 1])
print(solution(['A', 'A', 'B'], [600, 500, 300]) == [0, 1, 2])
print(solution(['A', 'B', 'A'], [600, 500, 600]) == [0, 2, 1])
print(solution(['A', 'B', 'A'], [600, 500, 700]) == [2, 0, 1])
print(solution(['A', 'A', 'A'], [600, 500, 700]) == [2, 0])
print(solution(['A', 'A', 'A'], [3, 2, 1]) == [0, 1])
print(solution(['classic', 'pop', 'classic', 'classic', 'pop'],
               [500, 600, 150, 800, 2500]) == [4, 1, 3, 0])
print(solution(['classic'], [2500]) == [0])
print(solution(['A', 'B', 'C'], [1, 2, 3]) == [2, 1, 0])
print(solution(['A', 'B', 'C', 'D'], [1, 2, 3, 1]) == [2, 1, 0, 3])
print(solution(['A', 'A', 'B', 'A'], [2, 2, 2, 3]) == [3, 0, 2])
print(solution(['A', 'A', 'B', 'A'], [5, 5, 6, 5]) == [0, 1, 2])
print(solution(['A', 'A', 'B', 'A', 'B', 'B'], [5, 5, 6, 5, 7, 7]) == [4, 5, 0, 1])