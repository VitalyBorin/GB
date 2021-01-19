class Auto:

    def __add__(self, other):
        return 'Машины столкнулись !!!'

zaz = Auto()
ferrari = Auto()

print(zaz + ferrari)