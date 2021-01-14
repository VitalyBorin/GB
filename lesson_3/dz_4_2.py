x = int(input('Введите действительное положительное число x '))
y = int(input('Введите целое отрицательное число y '))

def my_func_4_1(a, b):
    res = 1
    while b != 0:
        res = res / a
        b += 1
    return res

if x < 0 or y > -1:
    print('Введены неверные числа')
print ('x в степени y - ' + str(my_func_4_1(x, y)))