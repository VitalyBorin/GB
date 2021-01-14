def my_second_func (name, last_name, year_of_born, city, email, phone):
    print(f'Сведения о пользователе: Имя - {name}, Фамилия - {last_name}, Год рождения - {year_of_born}, город - {city}, email - {email}, телефон - {phone}')

a = input('Введите имя ')
b = input('Введите фамилию ')
c = input('Введите год рождения ')
d = input('Введите город ')
e = input('Введите email ')
f = input('Введите телефон ')

my_second_func(last_name=b, name=a, city=d, phone=f, email=e, year_of_born=c)

