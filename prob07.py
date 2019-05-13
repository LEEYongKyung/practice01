# 키보드에서 5개의 정수를 입력 받고 평균을 구하는 프로그램을 작성하시오

import sys
l = []
s = 0

for cnt in range(5):


    num = input('{}번째 수를 입력하세요: '.format(cnt+1))
    if num.isdigit() is False:
        print('ERRor')
        sys.exit(0)
    l.append(int(num))



print(sum(l, 0)/len(l))




