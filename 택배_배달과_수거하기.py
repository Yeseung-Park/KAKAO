cap = 4
n = 5
deliveries = [1, 0, 3, 1, 2]
pickups = [0, 3, 0, 4, 0]

def solution(cap, n, deliveries, pickups):
    '''
    한 번 담았을 때 최대한 몇 개까지 보낼 수 있는지 뒤에서부터 세자.
    앞에서부터 차례대로 보내고 가져오는 것도 차례대로 가져오기?
    '''
    answer = 0    # 답

    # 한 번에 배달할 순서 찾기
    deliveries_number = []
    temp_list = []    # 한 번에 배달할 집들을 담는 리스트
    temp = 0    # cap을 넘으면 초기화
    for i in range(n-1, -1, -1):
        if deliveries[i] == 0:    # 0이면
            continue    # 넘어가기
        if temp + deliveries[i] > cap:    # 최대 수용량을 넘어서면
            temp_list.sort()
            deliveries_number.append(temp_list)
            temp = 0
            temp_list = []    # 다 초기화해주고
            temp += deliveries[i]
            temp_list.append(i+1)
        else:
            temp += deliveries[i]
            temp_list.append(i+1)
    temp_list.sort()
    deliveries_number.append(temp_list)    # 마지막에도 한 번 더 넣기

    # 한 번에 수거할 순서도 찾기
    pickups_number = []
    temp_list = []
    temp = 0
    for i in range(n-1, -1, -1):
        if pickups[i] == 0:
            continue
        if temp + pickups[i] > cap:
            temp_list.sort()
            pickups_number.append(temp_list)
            temp = 0
            temp_list = []
            temp += pickups[i]
            temp_list.append(i+1)
        else:
            temp += pickups[i]
            temp_list.append(i+1)
    temp_list.sort()
    pickups_number.append(temp_list)


    print(deliveries_number)
    print(pickups_number)

    answer = -1
    return answer

solution(cap, n, deliveries, pickups)