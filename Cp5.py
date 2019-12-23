import Cp8
# color = input('Write Color')
# if color.lower() == 'green':
#     print('got 5')
# elif color.lower() == 'blue':
#     print('got 10')
# else:
#     print('got 20')

currUsers = ['aa', 'bb', 'cc', 'dd', 'ee']
newUsers = ['ff','a','bb','c','d']

for user in newUsers:
    if user.lower() in currUsers:
        print('invalid name')
    else:
        print('valid name')

Cp8.show_magicians(['All','Baby'])
