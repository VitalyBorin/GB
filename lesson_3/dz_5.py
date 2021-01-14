a = ''
b = []
m = 0
c = 0

while c != 111:
    a = input('Введите числа, разделенные пробелом ')
    b = a.split()
    for i in range(len(b)):
        if b[i] == '!':
            c = 111
        else:
            m += int(b[i])
    b.clear()
    print(m)