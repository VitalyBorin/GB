a = [True, 1, 'привет']
b = 0
dict = {'bool': 'булевая', 'int': 'целочисленная', 'str': 'строковая'}
for el in a:
    print(el, end='')
    print(' - '+dict.get(str(type(a[b])).split("'")[1]))
    b += 1
