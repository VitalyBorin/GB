def fact(a):
    res = []
    r = 1
    for el1 in range(a):
        r = r * (el1+1)
        res.append(r)
    yield res

n = input('Введите число n, при котором нужно рассчитать ряд от 1! до n! ')
n = int(n)
for el in fact(n):
    print (el)
