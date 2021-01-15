def int_func(s):
    if s.islower():
        return s.capitalize()
    else:
        return 'Введены неверные данные. Необходимо ввести строку мелкими латинскими буквами'

a = input('Введите несколько слов маленькими латинскими буквами, разделив их пробелами')
a = a.split()
for el in a:
    print(int_func(el), end=' ')