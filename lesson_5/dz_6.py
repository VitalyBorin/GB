import re

d = {}
pred = []
with open('file6.txt', 'r', encoding='utf-8') as f:
    for el in f:
        # пример поиска чисел в строке утащил из интернетов
        d[el.split(':')[0]] = sum([int(i) for i in re.findall(r'\d+', el)])
print (d)
