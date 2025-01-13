# 1
def print_params(a = 1, b = 'string', c = True):
    print(a,b,c)

print_params()
print_params(3, 'stroka')
# print_params(2, 'str', False, 32) - ошибка: больше параметров, чем есть в функции
print_params(b = 25)
print_params(c = [1,2,3])

print('_______')

# 2
values_list = [4, 'tri', False]
values_dict = {'a': 5, 'b': 'dva', 'c': True}
print_params(*values_list)
print_params(**values_dict)

print('_____')

#3
values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)