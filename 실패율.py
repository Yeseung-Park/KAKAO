N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]

def solution(N, stages):

    stage_failure = {}    # 스테이지별 실패율 담는 딕셔너리
    total = len(stages)    # 스테이지에 도달한 사용자 수
    answer = [0]*N

    # 접근 방식은 스테이지를 하나씩 넘어가면서 해당 스테이지에 위치해 있는 사람의 수를 구하고
    # 그걸 total로 나누어주면 된다. 스테이지를 넘어갈 때마다 이전에 고려했던 사용자 수를 빼주면
    # 그게 곧 현재 스테이지에 도달한 사용자 수가 되니까...
    # 뭔 말 알...? 나도 GPT가 한참 전에 알려준 거 기억을 끄집어내서 쓰는거라 설명이 쉽지는 않지만
    # 그냥 나 혼자만 읽을건데 이해 안 되어도 어쩔건데....

    for i in range(1, N+1):    # 실패율 구하기
        reach = stages.count(i)
        if total == 0:
            stage_failure[i] = 0
        else:
            stage_failure[i] = reach/total
        total -= reach    # 현재 스테이지에 머물러 있는 사람을 전체 사람에서 빼주기

    # 정렬하는 과정 기억하자
    stage_failure_sort = sorted(stage_failure.items(), key=lambda x: x[1], reverse=True)

    for i in range(N):
        answer[i] = stage_failure_sort[i][0]

    return answer

solution(N, stages)
