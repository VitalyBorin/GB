def int_func(s):
    if s.islower():
        return s.capitalize()
    else:
        return 'Введены неверные данные. Необходимо ввести строку мелкими латинскими буквами'

s = input('Введите слово маленькими латинскими буквами ')
print(int_func(s))