# 주어진 if 문을 dict를 사용하도록 수정하세요.

menu = input('메뉴: ')

# if menu == '오뎅':
#     price = 300
# elif menu == '순대':
#     price = 400
# elif menu == '만두':
#     price = 500
# else:
#     price = 0

#닥셔너리 사용
menu_dict =dict()

menu_dict = {'오뎅':300,'순대':400,'만두':500}
# if menu == '오뎅':
#     menu_dict['오뎅'] = 300
# elif menu == '순대':
#     menu_dict['순대'] = 400
# elif menu == '만두':
#     menu_dict['만두'] = 500
# else:
#     price=0

#
# if menu in menu_dict:
#     price = menu_dict[menu]
# else:
#     price = 0
# print('가격: {0}'.format(menu_dict[price]))

print('가격: {0}'.format(menu_dict[menu] if menu in menu_dict else 0))

