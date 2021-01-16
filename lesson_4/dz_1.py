from sys import argv

res = 0
script_name, working_hrs, money_of_hr, bonus = argv

res = float(working_hrs)*float(money_of_hr)+float(bonus)
print('Заработная плата составит ' + str(res) + '$')