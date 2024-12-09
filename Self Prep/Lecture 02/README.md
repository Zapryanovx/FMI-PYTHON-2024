# Python Основи: Обяснения и Примери

## Какъв ще е резултатът от следните операции?

```python
print(3 / 2)  # 1.5
print(3 // 2)  # 1
print(0.1 + 0.2)  # 0.30000000000000004
print(0.1 + 0.1)  # 0.2
print(0.5 - 0.2)  # 0.3
print(0.3 / 3)  # 0.09999999999999999
```

**[Note]** Важно е да се отбележи, че има особености при дробните числа поради представянето им в паметта (представят се в двоичен формат вместо десетичен и някои такива не могат да бъдат точно представени).

---

## Какъв е типът?

```python
things = ['eggs', ('spam', 'spam', 'spam'), 'ham']
print(type(things[1][2][3]))  # <class 'str'>
print(things[1][2][3])  # 'm'
```
**В Python няма тип `char`, има само `str` (низ).**

### Грешки при immutable обекти:

```python
things = ['eggs', ('spam', 'spam', 'spam'), 'ham']
try:
    things[1][2][3] = 'h'
except TypeError as err:
    print(str(err))  # 'str' object does not support item assignment
```

---

## Низовете също са immutable

```python
print(type(things[1][2][3]))  # <class 'str'>
```

---

## Mutable vs Immutable

### Списъците са mutable (можем да променяме техните елементи):

```python
things[1] = 'ham'
print(things)  # ['eggs', 'ham', 'ham']
```

### Кортежите са immutable (не можем да променяме техните елементи):

```python
things[1] = ('spam', 'spam', 'spam')  # Ако не го върнем към началното състояние, отново ще имаме случая, в който не можем да променим string.
try:
    things[1][2] = 'ham'  # things[1] е tuple (immutable) => не можем да променим негов елемент.
except TypeError as err:
    print(str(err))  # 'tuple' object does not support item assignment
```

---

## `is` vs `==`

- **`is`** проверява дали е една и съща инстанция.
- **`==`** проверява дали съдържанието на двете инстанции е едно и също (може двете инстанции да са една).

### Пример:

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)  # True - съдържанието е едно и също
print(a is b)  # False - различни обекти
print(a == c)  # True - съдържанието е едно и също
print(a is c)  # True - сочат към един и същ обект
```

---

## Списъците съдържат "референции" към елементи.

```python
coffee, cheese, crackers, tea = 'coffee', 'cheese', 'crackers', 'tea'

# Unpacking
things_i_like = [coffee, cheese, crackers]
things_you_like = [crackers, coffee, tea]

print(things_i_like[0] == things_you_like[1])  # Съдържанието е едно и също => True
print(things_i_like[0] is things_you_like[1])  # И двете сочат към едно и също нещо => True

things_i_like[0] = 'kafe'  # Това пренасочва референцията на първата клетка към 'kafe', не променя обекта coffee

print(things_i_like[0] == things_you_like[1])  # Съдържанието вече не е едно и също => False
print(things_i_like[0] is things_you_like[1])  # Вече сочат към различни неща => False
```

---

## Също така

```python
coffee, cheese, crackers, tea = 'coffee', 'cheese', 'crackers', 'tea'

things_i_like = [coffee, cheese, crackers]
things_you_like = [crackers, coffee, tea]

print(things_i_like[0] == things_you_like[1])  # Съдържанието е едно и също => True
print(things_i_like[0] is things_you_like[1])  # И двете сочат към едно и също нещо => True

things_i_like[0] = 'coffee'  # Това пренасочва референцията на първата клетка към 'coffee', не променя обекта coffee

print(things_i_like[0] == things_you_like[1])  # Съдържанието е едно и също => True
print(things_i_like[0] is things_you_like[1])  # И двете сочат към едно и също нещо ('coffee') => True
```

---


## Списък с референция към себе си

```python
cheeses = ['brie', 'bergkäse', 'kashkaval', 'leipäjuusto']
cheeses.append(cheeses)
cheeses[-1] is cheeses  # True
print(cheeses)  # ['brie', 'bergkäse', 'kashkaval', 'leipäjuusto', [...]]
```

Списъкът `cheeses` има референция към себе си на позиция 4, което създава бездънна рекурсия.

```python
print(cheeses[4][4][4][4][4][4][4][4][4][4][0])  # brie
```

### Прекъсване на рекурсията

Ако заменим елемента на позиция 4, рекурсията ще се прекъсне, тъй като `cheeses[4]` е референция.

```python
cheeses[4][4][4][4][4][4][4][4][4][4] = 'neshto'
print(cheeses)  # ['brie', 'bergkäse', 'kashkaval', 'leipäjuusto', 'neshto']
```

След прекъсване на рекурсията:

```python
try:
    cheeses[4][4][4][4][4][4][4][4][4][4] = 'neshto'
except IndexError as err:
    print(str(err))  # string index out of range
```

---

## Unpacking

```python
(a, b) = 1, 2
print(a)  # 1

a, b = 1, 2
print(a)  # 1

numbers = (1, 2, 3)
a, b, c = numbers
print(a)  # 1

a, *b, c = 1, 2, 3, 4, 5
print(a)  # 1
print(b)  # [2, 3, 4]
print(c)  # 5
```

`*b` сигнализира, че `b` ще разопакова символите между `a` и `c`. Например:

```python
try:
    a, b, c = 1, 2, 3, 4, 5
except ValueError as err:
    print(str(err))  # too many values to unpack (expected 3)
```

---

## Не можем да сравняваме tuple и list

```python
try:
    print((1, 2) < [1, 2])
except TypeError as err:
    print(str(err))  # '<' not supported between instances of 'tuple' and 'list'
```

---

## Множества

### Обединение на множества

```python
print({1, 2, 3} | {2, 3, 4})  # {1, 2, 3, 4}
```

### Пресичане на множества

```python
print({1, 2, 3} & {2, 3, 4})  # {2, 3}
```

### Разлика на множества

```python
print({1, 2, 3} - {2, 3, 4})  # {1}
```

### Симетрична разлика на множества

```python
print({1, 2, 3} ^ {2, 3, 4})  # {1, 4}
```

### Проверка дали едно множество е подмножество на друго

```python
print({1, 2, 3} < {2, 3, 4})  # False
print({2, 3} < {2, 3, 4})     # True
```

### Сравнение на множества

```python
print({2, 3} == {2.0, 3})     # True
```

---
