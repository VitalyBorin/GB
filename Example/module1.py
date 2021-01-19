class Test:
    count = 0

    def __init__(self):
        print('Я новый объект')
        # self.param = param
        self.param = 123
        Test.count += 1

obj1=Test()
obj2=Test()
obj3=Test()

print(obj1.count)

print(obj1.param)
print(obj2.param)
print(obj3.param)
obj1.param = 555

print('--------------------')

print(obj1.param)
obj1.count = 123
print(obj1.count)
print(obj2.count)

# obj1.param = 111
# obj2.param = 777
# print(type(obj1))