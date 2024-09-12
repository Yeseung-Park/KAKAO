dartResult = '1S2D*3T'

def solution(dartResult):

    darts_score = []    # 점수를 각각 담는 리스트
    score = ''
    temp = ['-']*3
    for i in range(len(dartResult)):
        if dartResult[i].isdecimal():    # 숫자면 점수
            score += dartResult[i]
        elif dartResult[i].isalpha():    # 알파벳이면 보너스
            if dartResult[i] == 'S':
                temp = int(score)
            elif dartResult[i] == 'D':
                temp = (int(score))**2
            elif dartResult[i] == 'T':
                temp = (int(score))**3
            score = ''
            darts_score.append(temp)    # 일단 알파벳 나오면 옵션을 제외한 점수는 계산했다는거니까 넣어주기
        else:    # 그 외에는 옵션인데 있을 수도 있고 없을 수도 있음
            if dartResult[i] == '*':
                if len(darts_score) == 1:
                    darts_score[-1] *= 2
                else:
                    darts_score[-1] *= 2
                    darts_score[-2] *= 2
            elif dartResult[i] == '#':
                darts_score[-1] *= (-1)

    answer = sum(darts_score)

    return answer

solution(dartResult)
