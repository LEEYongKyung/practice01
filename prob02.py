# 키보드로 정수 수치를 입력 받아 짝수인지 홀수 인지 판별하는 코드를 작성하세요.
import sys

while True:
    number = input('수를 입력하세요: ')
    if number.isdigit() is False:
        print('정수가 아닙니다.\n')
        sys.exit(0)

    number = int(number)
    if number& 0X0001 == 0:
        print("짝수\n")
    else:
        print("홀수\n")
