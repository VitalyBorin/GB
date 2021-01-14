def my_3rd_func(a, b, c):
    m = set([a, b, c])
    m1 = max(m)
    m.discard(m1)
    m2 = max(m)
    return m1 + m2
print(my_3rd_func(5555555555555555, 12111113123, 300000))