str_1 = [1,2,3,3,3,2,2,1,1,6,9]
str_2 = []
str_2 = [i for i in str_1 for j in str_2 if i != j]

print(str_1)
print(str_2)
