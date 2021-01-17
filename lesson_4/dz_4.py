a = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
b = []
print(a)
flag = 0

# b = [el for el in a for el2 in a if el == el2]
# не придумал как сделать в одну строку. Почему-то не работает

for el in a:
    for el2 in a:
        if el == el2:
            flag += 1
    if flag < 2:
        b.append(el)
    flag = 0

print(b)
