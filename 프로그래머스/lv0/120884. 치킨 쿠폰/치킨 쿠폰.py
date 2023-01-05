def solution(chicken):
    answer = 0
    while(chicken>9):
        answer += int(chicken/10)
        coupon = int(chicken/10)
        chicken = chicken%10 + coupon
    
    return answer