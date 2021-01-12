a = input('Введите строку из слов, разделенных пробелами ')
b = 1
for el in a.split():
    print(str(b) + ' ' + el[0:10])
    b += 1