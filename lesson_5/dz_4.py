in_f = open("in_file.txt", 'r', encoding='utf-8')
out_f = open("out_file.txt", 'w', encoding='utf-8')
for line in in_f:
    line=line.replace('One', "Один")
    line=line.replace('Two', "Два")
    line=line.replace('Three', "Три")
    line=line.replace('Four', "Четыре")
    print(line, file=out_f)