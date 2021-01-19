import json

firm = {}
av = []
with open('file7.txt', 'r', encoding='utf-8') as f:
    for el in f:
        mas = el.split()
        profit = float(mas[2]) - float(mas[3])
        firm[mas[0]] = profit
        if profit > 0:
            av.append(profit)

fin_list = [firm, {'average_profit' : sum(av)/len(av)}]

with open('file7.json', 'w') as f2:
    json.dump(fin_list, f2)