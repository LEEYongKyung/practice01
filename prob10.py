# 숫자를 입력 받아서 아래와 같은 실행결과가 나타나도록 코드를 완성하세요.
import sys

while True:
    number = input('숫자를 입력하세요 : ')

    if(number.isdigit()) is False:
        break

    number = int(number)
    i = 0
    s = 0
    iseven = number & 0x0001 ==0

    s =0
    for n in range(number+1):
        if iseven and n & 0x0001 == 0:
            s +=n
        elif not iseven and n & 0x0001 == 1:
            s +=n
    print('결과 : {0}'.format(s))


    #     while i <= number:
    #         if i %2 ==0:
    #             s += i
    #         i += 1
    #     print('결과 값: ',s)
    #
    # else:
    #
    #     while i <= number:
    #         if i %2 !=0:
    #             s += i
    #         i += 1
    #     print('결과 값: ',s)







