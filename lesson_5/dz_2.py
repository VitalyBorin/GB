rows = 0
words = 0
with open('asd.txt', 'r') as f:
    for l in f:
        # l = f.readline()
        rows += 1
        w = l.split()
        words += len(w)
print(f'В файле {rows} строк и {words} слов')