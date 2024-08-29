new_id = "...!@BaT#*..y.abcdefghijklm"

def solution(new_id):

    # 1단계 - 모든 대문자를 소문자로 바꾸기
    new_id = new_id.lower()

    # 2단계 - 영어 소문자, 숫자, -, _, . 만 남기기
    possible_id = ''
    for str in new_id:
        if str.isalpha() == True or str.isdecimal() == True:
            possible_id += str
        elif str in ['-', '_', '.']:
            possible_id += str
    new_id = possible_id

    # 3단계 - 마침표가 두 번 이상 연속되면 하나의 마침표로 변경
    possible_id = ''
    for str in new_id:
        if possible_id == '':
            possible_id += str
        else:
            if str == '.':
                if possible_id[-1] == '.':
                    pass
                else:
                    possible_id += str
            else:
                possible_id += str
    new_id = possible_id

    # 4단계 - 처음이나 끝이 . 일 경우 제거
    new_id = list(new_id)
    if len(new_id) != 0:
        if new_id[0] == '.':
            new_id.pop(0)
    if len(new_id) != 0:
        if new_id[-1] == '.':
            new_id.pop()
    new_id = ''.join(new_id)

    # 5단계 - 빈 문자열이면 a를 대입
    if new_id == '':
        new_id = 'a'
    else:
        pass

    # 6단계 - 16자 이상이면 첫 15개만 혀용
    if len(new_id) >= 16:
        new_id = new_id[0:15]

    # 15개로 잘랐을 때 맨 뒤에 . 이 오게 되는 경우가 생기므로 끝부분에 대해서 4단계를 한 번 더 거치기
    new_id = list(new_id)
    if len(new_id) != 0:
        if new_id[-1] == '.':
            new_id.pop()

    # 7단계 - 길이가 2자 이하라면 길이가 3이 될 때까지 마지막 문자 반복
    if len(new_id) <= 2:
        while len(new_id) != 3:
            new_id.append(new_id[-1])
    new_id = ''.join(new_id)

    return new_id

solution(new_id)