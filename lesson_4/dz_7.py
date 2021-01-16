# fact = (param * param for param in range(5))
#
# for el in fact():
#     print(el)

def fact(n):
    res = 1
    for el in range(n):
        res = res * (el + 1)
    yield res

g=fact()
for el in g(n)
    # print(fact(4))
print(g())





# def fact():
#     i =
#     yield el
#
#
# for el in fact(n)
#