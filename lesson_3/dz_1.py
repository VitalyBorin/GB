def my_func(arg1, arg2):
    div_res = 0
    if arg2 == 0:
        print ('На ноль делить нельзя!!!')
        return
    else:
        div_res = arg1 / arg2
        return div_res

arg1 = int(input('Введите первое число '))
arg2 = int(input('Введите второе число '))

if my_func(arg1, arg2) == None:
    print('Результат деления первого числа на второе ' + str(my_func(arg1, arg2)))