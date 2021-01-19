a = ' '
with open("file.txt", "w") as f:
    while a != '':
        a = input('Введите строку и нажмите Enter для записи строки в файл. При вводе пустой строки запись в файл прекратится')
        print(a, file=f)