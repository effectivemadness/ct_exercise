def solution(brown, yellow):
    answer = []
    # 가로 늘려가면서 테스트
    x = 3
    y = 3
    while True:
        x = 3
        while True:
            yellow_calc = (x-2) * (y-2)
            brown_calc = x*y - yellow_calc
            print(x, y, brown_calc, yellow_calc)
            if brown > brown_calc:
                x+=1
            elif brown_calc == brown and yellow_calc == yellow:
                return [x, y]
            else: 
                break
        y += 1
    return answer

print(solution(24,24))