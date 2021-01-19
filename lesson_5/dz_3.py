salary_list=[]
salary_sum=0
l=[]
with open('salary.txt', 'r', encoding='utf-8') as f:
    for line in f:
        l=line.split()
        if float(l[1]) < 20000:
            salary_list.append(l[0])
            salary_sum += float(l[1])

salary_sum = salary_sum / (len(salary_list)+1)
print('Фамилии сотрудников зп меньше 20К ', salary_list)
print('Их средняя заработная плата ', float(salary_sum))