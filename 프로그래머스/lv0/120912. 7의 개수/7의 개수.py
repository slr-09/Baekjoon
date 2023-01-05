def solution(array):
    answer = 0
    for i in range(len(array)):
        ch = str(array[i])
        for j in range(len(ch)):
            if int(ch[j])==7:
                answer += 1
    return answer