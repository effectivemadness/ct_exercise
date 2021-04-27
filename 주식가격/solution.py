def solution(prices):
    answer = []
    for i in range(len(prices)):
        j = i
        while j < len(prices):
            print(i,j)
            if prices[i] > prices[j]:
                j+=1
                print(prices[j-1]," is down for ",prices[i])
                break
            j+=1
        j-=1
        answer.append(j-i)
    return answer

print(solution([1, 2, 3, 2, 3]))