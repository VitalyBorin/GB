my_list = []

# Заведем данные в структуру
a = 1
for i in range(3):
    name_eq = input('Введите название товара ' + str(i+1) + ' ')
    price_eq = input('Введите цену товара ' + str(i+1) + ' ')
    count_eq = input('Введите количество товара ' + str(i+1) + ' ')
    piece_eq = input('Введите единицу измерения товара ' + str(i+1) + ' ')
    my_dict = {'название': name_eq, 'цена': price_eq, 'количество': count_eq, 'ед': piece_eq}
    my_turple = (a, my_dict)
    my_list.append(my_turple)
    a += 1
print(my_list)

# Перелопатим данные в другую кривую структуру
new_dict = {'название': [list(my_list[0])[1].get('название'), list(my_list[1])[1].get('название'), list(my_list[2])[1].get('название')], 'цена': [list(my_list[0])[1].get('цена'), list(my_list[1])[1].get('цена'), list(my_list[2])[1].get('цена')], 'количество': [list(my_list[0])[1].get('количество'), list(my_list[1])[1].get('количество'), list(my_list[2])[1].get('количество')], 'ед': [list(my_list[0])[1].get('ед'), list(my_list[1])[1].get('ед'), list(my_list[2])[1].get('ед')]}
print(new_dict)
