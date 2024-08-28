today = "2022.05.19"
terms = ["A 6", "B 12", "C 3"]
privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]

def solution(today, terms, privacies):
    today_list = list(map(int, today.split('.')))   # today_list[0]->연, today_list[1]->월, today_list[2]->일
    terms_dict = {}    # 약관: 유효기간 딕셔너리
    answer = []

    # 딕셔너리 채우기
    for term in terms:
        terms_dict[term.split(' ')[0]] = int(term.split(' ')[1])

    # 하나씩 찾아보기
    for i in range(len(privacies)):
        date, term = privacies[i].split(' ')[0], privacies[i].split(' ')[1]
        date = list(map(int, date.split('.')))
        expired_date = date[:]

        # 마감 날짜 계산하기
        expired_date[0] += terms_dict[term] // 12
        expired_date[1] += terms_dict[term] % 12
        expired_date[2] -= 1
        if expired_date[2] == 0:
            expired_date[1] -= 1
            expired_date[2] = 28
        if expired_date[1] > 12:    # 달이 12보다 더 크다면
            expired_date[1] -= 12
            expired_date[0] += 1

        if today_list[0] > expired_date[0]:    # 연이 더 크면 뒤에 비교하지 않아도 유효기간 넘어선 것
            answer.append(i+1)
        elif today_list[0] == expired_date[0]:    # 연이 같을 경우
            if today_list[1] > expired_date[1]:    # 월이 더 크면 뒤에 비교하지 않아도 유효기간 넘어선 것
                answer.append(i+1)
            elif today_list[1] == expired_date[1]:    # 월도 같을 경우
                if today_list[2] > expired_date[2]:    # 일이 더 크면
                    answer.append(i+1)

    return answer

solution(today,terms,privacies)