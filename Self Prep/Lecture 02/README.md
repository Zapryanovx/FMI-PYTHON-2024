# Python Основи: Обяснения и Примери

## 1. Операции с числа

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

## 2. Типове в Python

```python
things = ['eggs', ('spam', 'spam', 'spam'), 'ham']
print(type(things[1][2][3]))  # <class 'str'>
print(things[1][2][3])  # 'm'
```
**В Python няма тип `char`, има само тип `str` (низ).**

### Грешки при immutable обекти:

```python
things = ['eggs', ('spam', 'spam', 'spam'), 'ham']
try:
    things[1][2][3] = 'h'
except TypeError as err:
    print(str(err))  # 'str' object does not support item assignment
```

---

## 3. Mutable vs Immutable

### Списъците са mutable (можем да променяме техните елементи):
```python
things[1] = 'ham'
print(things)  # ['eggs', 'ham', 'ham']
```

### Кортежите са immutable (не можем да променяме техните елементи):
```python
things[1] = ('spam', 'spam', 'spam')
try:
    things[1][2] = 'ham'
except TypeError as err:
    print(str(err))  # 'tuple' object does not support item assignment
```

---

## 4. Операторите `is` и `==`

- **`is`** проверява дали е една и съща инстанция.
- **`==`** проверява дали съдържанието на две инстанции е едно и също.

### Пример:

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)  # True - съдържанието е едно и също
print(a is b)  # False - различни обекти
print(a == c)  # True - съдържанието е едно и също
print(a is c)  # True - сочат към един и същи обект
```

---

## 5. Референции в списъците

### Списъците съдържат референции към обекти:

```python
coffee, cheese, crackers, tea = 'coffee', 'cheese', 'crackers', 'tea'

things_i_like = [coffee, cheese, crackers]
things_you_like = [crackers, coffee, tea]

print(things_i_like[0] == things_you_like[1])  # True - съдържанието е същото
print(things_i_like[0] is things_you_like[1])  # True - сочат към един и същ обект
```

### Промяна на референция:

```python
things_i_like[0] = 'kafe'  # Променяме референцията на първата клетка

print(things_i_like[0] == things_you_like[1])  # False - съдържанието е различно
print(things_i_like[0] is things_you_like[1])  # False - сочат към различни обекти
```

---

## 6. Допълнителен пример:

```python
coffee, cheese, crackers, tea = 'coffee', 'cheese', 'crackers', 'tea'

things_i_like = [coffee, cheese, crackers]
things_you_like = [crackers, coffee, tea]

print(things_i_like[0] == things_you_like[1])  # True - съдържанието е същото
print(things_i_like[0] is things_you_like[1])  # True - сочат към един и същ обект

things_i_like[0] = 'coffee'  # Променяме референцията

print(things_i_like[0] == things_you_like[1])  # True - съдържанието е същото
print(things_i_like[0] is things_you_like[1])  # True - сочат към един и същ обект
```

---
