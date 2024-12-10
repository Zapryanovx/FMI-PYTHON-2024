
# Концепции и примери с Python

Това хранилище изследва различни концепции на Python чрез практически примери, включително декоратори, класови методи, статични методи, свойства и други.

---

## Декоратори

Декораторите модифицират поведението на функции или методи. Следният пример демонстрира две еквивалентни имплементации на декоратори:

```python
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
```

---

## Статични методи

Статичните методи се дефинират чрез `@staticmethod`. Те не изискват достъп до инстанция или до самия клас. Те функционират като обикновени функции, но са дефинирани вътре в клас за по-добра организация.

Пример: методът `from_list` в класа `Vector`.

```python
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
print(Vector.length(v1))
```

---

## Класови методи

Класовите методи се дефинират чрез `@classmethod` и приемат класа като първи аргумент (`cls`). Те могат да достъпват или променят данни на ниво клас и могат да бъдат извиквани както от класа, така и от неговите инстанции.

Пример:

```python
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
```

Друг пример:

```python
class Example:
    @classmethod
    def class_method(cls):
        print(f"Class method called.")

Example.class_method()

example_instance = Example()
example_instance.class_method()
```

---

## Свойства (Properties)

Свойствата позволяват методите да бъдат достъпвани като атрибути чрез декоратора `@property`. Те също така могат да имат setter функционалност.

Пример със `length`:

```python
import math

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def length(self):
        return math.sqrt(self.x**2 + self.y**2)

spam = Vector(1.0, 2.0)
print(spam.length)
```

Друг пример с getter и setter:

```python
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
```

---

## Сравнение и методи на инстанция

По подразбиране, `__eq__` се имплементира чрез `is`, така че две инстанции на един и същ клас се считат за различни, освен ако това не бъде изрично променено.

Пример:

```python
v1 = Vector(1.0, 2.0, 3.0)
v2 = Vector(1.0, 2.0, 3.0)
print(v1 == v2)  # False
```

---

## Резюме

Тази колекция от примери илюстрира ключови концепции на Python и тяхното практическо приложение. Включени са декоратори, статични методи, класови методи, свойства и по-напреднали концепции като `getattr` и `setattr`.

Чувствайте се свободни да изследвате и модифицирате примерите, за да задълбочите знанията си за Python!
