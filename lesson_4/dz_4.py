a = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
b = []
print(a)
flag = False

# b = [el for el in a for el2 in b if el != el2]
# не придумал как сделать в одну строку. Почему-то не работает

for el in a:
    for el2 in b:
        if el == el2:
            flag = True
    if not flag:
        b.append(el)
    flag = False

print(b)