a = [7, 5, 3, 3, 2]
b = ''

while True:
    print('Для выхода нажмите * и Enter')
    b = input('Введите число ')
    if b == '*':
        break
    c = 0
    for el in a:
        if int(b) > el:
            a.insert(c, int(b))
            break
        elif c == len(a)-1:
            a.append(int(b))
            break
        c += 1
    print(a)