# Python Основи: Примери и Обяснения

## Речници: Създаване и достъп до ключове

```python
lectures_location = {'Tuesday': '101', 'Thursday': '200'}

lectures_location['Friday'] = '204'  # можем да създаваме нови ключове
print(lectures_location)  # {'Tuesday': '101', 'Thursday': '200', 'Friday': '204'}

lectures_location['Friday'] = '205'  # да променяме стойностите им
print(lectures_location)  # {'Tuesday': '101', 'Thursday': '200', 'Friday': '205'}

try: 
    lectures_location['Wednesday']  # но не можем да достъпваме такива, които ги няма
except KeyError as err:
    print(type(err), str(err))  # <class 'KeyError'> 'Wednesday'

# Ако имаме несъществуващ ключ
print(lectures_location.get('Wednesday', 'няма сряда'))  # няма сряда
print(lectures_location.get('Friday', 'няма сряда'))  # 205
```

---

## Кортежи: Immutable, но референциите могат да се променят

```python
other_things = (42, [1, 2, 3], 'baba')

try:
    other_things[1] += [4]  # Това се раздробява на two steps: добавя към списъка и се опитва да присвои
except TypeError as err:
    print(str(err))  # 'tuple' object does not support item assignment

print(other_things)  # (42, [1, 2, 3, 4], 'baba')
```

---

## Форматиране с f-стрингове

```python
main_character = "Captain Jack Sparrow"
print(f"This is the tale of {main_character}")  # "This is the tale of Captain Jack Sparrow"
```

### Подравняване и широчина на полетата
```python
heights = {"Mount Everest": 8849, "Musala": 2925, "Shaq": 2.16}
for name, height in heights.items():
    print(f"{name:15} ==> {height:10}")
```
- `15` в `{name:15}`: Резервира 15 символа за текста (подравнен наляво).
- `10` в `{height:10}`: Резервира 10 символа за числото (подравнено надясно).

---

## Булеви стойности и интерпретация

В контекста на булевите операции като "лъжа" се интерпретират:
- `False`
- `None`
- Числото `0` (вкл. `0.0`, `0j`)
- Празен низ `""`
- Празни колекции (`[]`, `{}`, `set()`)
- **Ваши обекти** могат да дефинират своето поведение.

Всички други стойности се интерпретират като "истина".

---

## Превръщане на обекти в низове с `str()`

```python
b = 10
print(str(b))  # '10'

nums = (1, 2, 3)
nums = list(nums)
print(nums)  # [1, 2, 3]

print(str(['baba', 2]))  # "['baba', 2]"
```

---

## Match-Case

```python
http_status = 400
match http_status:
    case 400:
        print("Bad request")
    case 401 | 403:
        print("Authentication error")
    case 404:
        print("Not found")
    case _:
        print("Other error")
```
- `case 401 | 403`: използва побитово `|` за "или".
- `case _`: дефинира "по подразбиране".

---

## Функции с именувани аргументи

```python
def f(a=5, b=10, c=15):
    print(c)

f(c=200, a=5.243, b=-1)  # Именуваните аргументи могат да се подават в произволен ред
```

---
