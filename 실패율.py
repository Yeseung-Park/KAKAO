N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]

def solution(N, stages):

    stage_reach = {}    # 스테이지별 도달한 플레이어 수를 담는 딕셔너리
    stage_stay = {}    # 스테이지별 도달했으나 클리어하지 못한 플레이어 수를 담는 딕셔너리
    stage_failure = {}    # 스테이지별 실패율을 담는 딕셔너리
    answer = [0]*N

    # stage_reach와 stage_stay의 기본 값을 만드는 부분
    for i in range(1, N+1):
        stage_reach[i] = 0
        stage_stay[i] = 0
        stage_failure[i] = 0

    for i in range(1, N+1):
        for stage in stages:
            if stage >= i:
                stage_reach[i] += 1
            if stage == i:
                stage_stay[i] += 1

    for i in range(1, N+1):
        if stage_reach[i] == 0:
            stage_failure[i] = 0
        else:
            stage_failure[i] = stage_stay[i]/stage_reach[i]

    stage_failure_sorted = sorted(stage_failure.items(), key=lambda x: x[1], reverse=True)

    for i in range(N):
        answer[i] = stage_failure_sorted[i][0]

    return answer

solution(N, stages)