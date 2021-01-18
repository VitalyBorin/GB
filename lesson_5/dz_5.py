import random

with open('file5.txt', 'w') as f:
    for el in range(100):
        print(str(random.randint(1,1000000)), end=' ', file=f)

# Представим, что здесь тысячи строк умного кода, на самом деле читаем из того же файла
sum = 0
with open('file5.txt', 'r') as f:
    l = f.read()
l = l.split()
for el in l:
    sum += int(el)
print (sum)