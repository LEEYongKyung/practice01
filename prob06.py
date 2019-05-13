# 키보드에서 정수로 된 돈의 액수를 입력 받아 오만 원권, 만원 권, 오천 원권, 천원 권, 500원짜리 동전, 100원짜리 동전,
# 50원짜리 동전, 10원짜리 동전, 1원짜리 동전 각 몇 개로 변환 되는지 작성하시오.

import sys

money = input('금액: ')
#
# if money.isdigit() is False:
#     print('수를 입력하십시오')
#     sys.exit(0)
# else:
#     money = int(money)
#     fiv_mil =0
#     one_mil = 0
#     fiv_thu =0
#     one_thu=0
#     fiv_hun=0
#     one_hun=0
#     fiv_ten=0
#     one_ten=0
#     five=0
#     one=0
#
#     fiv_mil, money = divmod(money,50000)
#     one_mil, money = divmod(money, 10000)
#     fiv_thu, money = divmod(money, 5000)
#     one_thu, money = divmod(money, 1000)
#     fiv_hun, money = divmod(money, 500)
#     one_hun, money = divmod(money, 100)
#     fiv_ten, money = divmod(money, 50)
#     one_ten, money = divmod(money, 10)
#     five, money = divmod(money, 5)
#     one, money = divmod(money, 1)
#
#     print("""
#     50000원 : {}개
#     10000원 : {}개
#     5000원: {}개
#     1000원: {}개
#     500원: {}개
#     100원: {}개
#     50원:{}개
#     10원:{}개
#     5원:{}개
#     1원:{}개
#
#
#     """.format(fiv_mil,one_mil,fiv_thu,one_thu,fiv_hun,one_hun,fiv_ten,one_ten,five,one))
    #
    # if money / 50000 !=0:
    #     money = money / 50000
    #     fiv_mil +=1
    #
    #     if money / 10000 !=0

if money.isdigit() is False:
    print('수를 입력하십시오')
    sys.exit(0)
money = int(money)
for won in [50000,10000,5000,1000,500,100,50,10,5,1]:
    count =money//won
    money -= count*won
    print("{0}월 {1}개".format(won,money))









