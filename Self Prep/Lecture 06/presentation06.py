# Следните два кода са еквивалентни

def wrapper(func):
    def decorator():
        return func
    return decorator

@(lambda spam: lambda: spam)
def eggs():
    print('Подръж ми яйцата!')

@wrapper
def eggs2():
    print('Подръж ми яйцата!')

print(eggs())
print(eggs2())

eggs()()
eggs2()()

print()
print()

def spam(spam):
    def spam():
        return spam
    return spam

@spam
def spam():
    return spam

print(spam()) # <function spam.<locals>.spam at 0x0000025E63428720>
print(spam()()) # <function spam.<locals>.spam at 0x0000025E63428720> (същото)


class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
    def _coords(self):
        return (self.x, self.y, self.z)
    
    def length(self):
        return sum(_ ** 2 for _ in self._coords()) ** 0.5

    @staticmethod
    def from_list(numbers):
        if len(numbers) != 3:
            pass
        return Vector(numbers[0], numbers[1], numbers[2])    

v1 = Vector(1.0, 2.0, 3.0)
v2 = Vector(1.0, 2.0, 3.0)
print(v1 == v2) #по подразбиране __eq__ е имплементиран с is => false (2 различни инстанции)
v3 = Vector(7.0, 8.0, 9.0)
print(Vector.length(v1)) 
print(Vector.length(v2))
print(list(map(Vector.length, [v1, v2, v3]))) #unbound method

v1 = Vector(1, 1, 1)
getattr(v1, 'y')
setattr(v1, 'z', 5)
getattr(v1, 'z')

#Статичните методи са методи, които не изискват информация нито за инстанция на клас, нито за самия клас,
#тоест функционират като обикновени функции, но просто са дефинирани вътре в класа, в случая
#from_list метода на Vector, не изисква информация за класа Vector или негова инстанция

class Countable:
    _count = 0
    def __init__(self, data):
        self.data = data
        type(self).increase_count()
   
    @classmethod
    def increase_count(cls):
        cls._count += 1
   
    @classmethod
    def decrease_count(cls):
        cls._count -= 1

#Клас методите са методи, които не изискват инстанция на класа и променя cls._count за всички инстанции на класа,
#също така клас методите могат да се извикват както от инстанции, така и от самия клас

class Example:

    @classmethod
    def class_method(cls):
        print(f"Class method called.")

Example.class_method() 

example_instance = Example()
example_instance.class_method()

#Property позволява на даден метод да се достъпва като атрибут, т.е.
#ако добавим дерокатора на функцията length:

# import math

# @property
# def length(self):
#     return math.sqrt(self.x**2 + self.y**2)

# spam = Vector(1.0, 2.0)
# print(spam.length)

class Color:
    def __init__(self, rgba):
        self._rgba = tuple(rgba)
    
    @property
    def rgba(self):
        return self._rgba
    
    @rgba.setter
    def rgba(self, value):
        self._rgba = tuple(value)
        
red = Color([255, 0, 0])
print(red.rgba)
red.rgba = [200, 0, 0]
print(red.rgba)