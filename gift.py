friends = ["muzi", "ryan", "frodo", "neo"]
gifts = ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]
# 준 사람, 받는 사람

def solution(friends, gifts):
    # 이차원 배열로 생각해볼까
    # friends 리스트의 i번째에 있던 사람을 i행, i열에 대응

    # 일단 선물 교환 이차원 배열 만들기
    gift_trade = [[0]*len(friends) for _ in range(len(friends))]
    gift_factor = {}    # 인당 선물지수를 담을 딕셔너리
    next_month_gift = {}    # 다음 달 인당 받을 선물의 개수를 담는 딕셔너리

    # 다음달 딕셔너리 기본 값 채우기
    for friend in friends:
        next_month_gift[friend] = 0
        gift_factor[friend] = 0

    # print(this_month_gift)

    # 선물 교환 이차원 배열 채우기
    # 선물 지수 딕셔너리 배열도 채우기
    # 행이 준 사람 열이 받은 사람
    for gift in gifts:
        temp = gift.split(" ")
        gift_give = friends.index(temp[0])
        gift_get = friends.index(temp[1])
        gift_trade[gift_give][gift_get] += 1
        gift_factor[temp[0]] += 1
        gift_factor[temp[1]] -= 1

    for i in range(len(friends)):
        for j in range(len(friends)):
            gift_give = friends.index(i)
            gift_get = friends.index(j)
            if i < j:
                # 우선 선물 주고받은 횟수 비교
                if gift_trade[i][j] > gift_trade[j][i]:    # i가 더 많이 준 것
                    next_month_gift[gift_give] += 1
                elif gift_trade[i][j] < gift_trade[j][i]:    # j가 더 많이 준 것
                    next_month_gift[gift_get] += 1
                else:    # 같을 경우
                    if gift_factor[gift_give] > gift_factor[gift_get]:


    print(gift_trade)
    print(gift_factor)


solution(friends, gifts)