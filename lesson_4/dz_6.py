from itertools import count
from itertools import cycle
my_list = ['Вася', 'Петя', 'Оля']

i = input('Введие исходное число ')
for el in count(int(i)):
    if el > 10:
        break
    else:
        print(el)

с = 0
for el in cycle(my_list):
    if с > 10:
        break
    print(el)
    с += 1