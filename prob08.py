# 문자열을 입력 받아, 해당 문자열을 문자 순서를 뒤집어서 반환하는 함수 reverse(s)을 작성하세요.

import sys
def reverse(s):
    # print('len = ',len(s))
    # out = []
    # st1 = ''
    #
    # for index in range(len(s)-1,-1,-1):
    #     print(index)
    #     # out.append(s[index])
    #     st1 += s[index]

    return s[::-1]





instr = input('입력> ')

print('결과> ' + reverse(instr))
