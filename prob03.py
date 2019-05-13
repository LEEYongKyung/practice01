# 다음과 같은 출력이 되도록 이중 for~in 문을 사용한 코드를 작성하세요.

# s = """
# *
# **
# ***
# ****
# *****
# ******
# *******
# ********
# *********
# **********
# """

# print(s)


#
# for y in range(0,10):
#     for x in range(0,y+1):
#         print('*',end=' ')
#      print('\n')

for i in range(1,11):
    print('*'*i)