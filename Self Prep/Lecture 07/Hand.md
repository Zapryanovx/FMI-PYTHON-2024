
# Работа с магически методи в Python (напр. __getitem__, __setitem__, __getattr__, __setattr__, __getattribute__)

Това хранилище съдържа примери за работа с магически методи в Python. Ще разгледаме основни концепции като достъп до атрибути, работа със специални методи и начини за манипулиране на инстанции на класове.

---

## Пример: Индексиране чрез __getitem__

Методът `__getitem__` позволява достъп до член-данните на обект чрез индексация (`obj[index]`).

```python
class Hand:
    def __init__(self):
        self.thumb = 'Палец'
        self.index_finger = 'Показалец'
        self.middle_finger = 'Среден'
        self.ring_finger = 'Безименен'
        self.pinkie = 'Кутре'
        
    def __getitem__(self, index):
        return (self.thumb, self.index_finger, self.middle_finger,
                self.ring_finger, self.pinkie)[index]

hand = Hand()
print(hand[4])  # Кутре
```

### Ограничения на __getitem__

`__getitem__` позволява достъп, но не промяна на атрибутите. Ако се опитате да промените стойност чрез индексация, ще получите грешка:

```python
hand = Hand()
try:
    hand[2] = 'кебапче'
except TypeError as err:
    print(str(err))  # 'Hand' object does not support item assignment
```

---

## Пример: Промяна на атрибути чрез __setitem__

За да позволим промяна на стойности чрез индексация, можем да дефинираме метода `__setitem__`:

```python
class Hand:
    def __init__(self):
        self.thumb = 'Палец'
        self.index_finger = 'Показалец'
        self.middle_finger = 'Среден'
        self.ring_finger = 'Безименен'
        self.pinkie = 'Кутре'
        
    def __getitem__(self, index):
        return (self.thumb, self.index_finger, self.middle_finger,
                self.ring_finger, self.pinkie)[index]
    
    def __setitem__(self, index, val):
        if index == 0:
            self.thumb = val
        elif index == 1:
            self.index_finger = val
        elif index == 2:
            self.middle_finger = val
        elif index == 3:
            self.ring_finger = val
        elif index == 4:
            self.pinkie = val

hand = Hand()
hand[1] = 'кебапче'
print(hand.index_finger)  # 'кебапче'
```

---

## Пример: __getattr__ за обработка на липсващи атрибути

Методът `__getattr__` се извиква само ако търсеният атрибут не съществува. Това позволява динамично обработване на липсващи атрибути.

```python
class Hand:
    def __init__(self):
        self.thumb = 'Палец'
        self.index_finger = 'Показалец'
        self.middle_finger = 'Среден'
        self.ring_finger = 'Безименен'
        self.pinkie = 'Кутре'
    
    def __getattr__(self, name):
        return f"Това е ръка v1.0. Все още няма {name} :("

hand = Hand()
print(hand.middle_finger)  # Среден
print(hand.sixth_finger)  # Това е ръка v1.0. Все още няма sixth_finger :(
```

---

## Пример: __setattr__ за проследяване на промени

Методът `__setattr__` се извиква винаги при задаване на стойност на атрибут. За да избегнем безкрайна рекурсия, използваме `object.__setattr__`:

```python
class Hand:
    def __setattr__(self, name, value):
        print(f"Нова стойност за {name} - {value}")
        object.__setattr__(self, name, value)

hand = Hand()
hand.pinkie = 'тест'
print(hand.pinkie)
```

---

## Пример: __getattribute__ за глобално обработване на достъпи

Методът `__getattribute__` се извиква при **всяко** търсене на атрибут. За да избегнем рекурсия, използваме `object.__getattribute__`:

```python
class Hand:
    def __getattribute__(self, name):
        print(f"Някой ми бърка по пръстите и иска {name}")
        return object.__getattribute__(self, name)

hand = Hand()
print(hand.pinkie)  # Някой ми бърка по пръстите и иска pinkie
```

---

## __dict__ и __class__

- **`__dict__`:** Речник, който съдържа всички атрибути на даден обект.
- **`__class__`:** Атрибут, който сочи към класа на обекта.

```python
hand = Hand()
print(hand.__dict__)  # {'thumb': 'Палец', 'index_finger': 'Показалец', ...}
print(hand.__class__)  # <class '__main__.Hand'>

print(Hand.__dict__)  # Съдържа методите и атрибутите на класа
```

---

## Обобщение

- `hand.__dict__`: Съдържа атрибутите, дефинирани в `__init__`.
- `Hand.__dict__`: Съдържа методите и останалите атрибути на класа.

Тези примери демонстрират как да използвате магическите методи за постигане на персонализирано поведение при работа с атрибути и индексация.
