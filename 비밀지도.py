n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]

def solution(n, arr1, arr2):
    '''
    1. arr1, arr2를 2진수로 바꾸기
    2. or 연산을 사용하기
    3. 결과를 #로 바꾸기
    '''
    bi_arr1 = []
    bi_arr2 = []    # 2진수로 바꾼 숫자들을 나열하는 리스트
    bi = []    # or 연산 이후의 2진수를 나열하는 리스트
    answer = []

    def decimal_to_binary(num):
        binary = ''
        while num > 0:
            remain = num % 2
            binary = str(remain) + binary
            num //= 2
        while len(binary) < n:
            binary = '0'+binary    # binary의 길이가 n이 될 때까지 0을 채워줘야 한다.
        return binary

    # 이진수로 바꾸기
    for i in range(n):
        bi_arr1.append(decimal_to_binary(arr1[i]))
        bi_arr2.append(decimal_to_binary(arr2[i]))

    # or 연산 시행하기
    for i in range(n):
        bi_num = ''
        for j in range(n):
            temp = int(bi_arr1[i][j])|int(bi_arr2[i][j])
            bi_num += str(temp)
        bi.append(bi_num)

    # 결과 도출하기
    for i in range(n):
        code = ''
        for j in range(n):
            if bi[i][j] == '1':
                code += '#'
            else:
                code += ' '
        answer.append(code)

    return answer

solution(n, arr1, arr2)

