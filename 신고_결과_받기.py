id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

def solution(id_list, report, k):

    id_report = {}    # 사용자와 신고 대상을 담는 딕셔너리
    id_reported = {}    # 사용자와 신고 당한 횟수를 담는 딕셔너리
    banned_list = []    # 실제로 정지당한 사용자의 리스트
    answer = [0]*len(id_list)

    for id in id_list:    # 딕셔너리 두 개의 기본값을 설정하는 과정
        id_report[id] = set()    # 중복된 신고는 하나로 처리하기 때문에 set()을 사용
        id_reported[id] = 0

    for r in report:    # 신고 대상을 딕셔너리에 담는 과정
        temp = r.split(' ')
        id_report[temp[0]].add(temp[1])

    for value in id_report.values():    # 사용자 별 신고당한 횟수를 딕셔너리에 담는 과정
        for id in value:
            id_reported[id] += 1

    for key, value in id_reported.items():    # 정지 당한 사용자를 찾아내는 과정
        if value >= k:
            banned_list.append(key)

    for banned in banned_list:    # 정지 당한 사용자를 신고한 사람을 찾고 메일 발송 횟수를 계산하는 과정
        for key, value in id_report.items():
            if banned in value:
                answer[id_list.index(key)] += 1

    return answer

solution(id_list, report, k)