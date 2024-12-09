# Python Основи: Обяснения и Примери
## `help()` - Извличане на документация
Функцията `help()` печата документацията на обекта, подаден в скобите. Документацията се съдържа в **docstring**-овете.
```python
print(help(5))  # Печата документацията за типа `int`
```
### Пример с функция
```python
def test():
    """eto edin"""
    
    print("""gotin primer""")
    
# help(test)
# Печата само docstring-овете, които описват функцията, т.е. стойността "eto edin".
```
---
## `dir()` - Атрибути и методи на обект
Функцията `dir()` се използва за извличане на списък с имената на атрибутите и методите, които са достъпни за даден обект.
```python
print(dir(5))  # Показва атрибутите и методите на обекта от тип `int`
```
> **[Note]** В Python всичко е обект.
---
## `type()` - Определяне на типа на обект
- `type(<тип>)` връща `<class 'type'>`.
- `type(type(<...>))` винаги връща `<class 'type'>`.
- В случая последното отпечатва `<class 'generator'>`, защото се извиква върху обект от тип генератор.
```python
print(type(map))  # <class 'type'>
print(type(filter))  # <class 'type'>
print(type(list))  # <class 'type'>
print(type(type("tip")))  # <class 'type'>
print(type((i for i in range(5))))  # <class 'generator'>
```
---
## Сравняване на обекти
- Можем да сравняваме различни типове числа:
```python
print(3 < 5.4)  # True
```
- Можем да сравняваме стрингове лексикографски:
```python
print("asd" < "asdd")  # True
print("asd" == "asd")  # True
```
---
## Референции в Python
В Python всичко е по референция:
```python
a = [1, 2, 3]
b = a
b.append(4)
print(a)  # [1, 2, 3, 4]
```
---
## Хетерогенни колекции
Колекциите в Python могат да съдържат елементи от различни типове:
```python
my_list = []
my_list.append('word')
my_list.append(5)
my_list.append(False)
print(my_list)  # ['word', 5, False]
```
---
## Slicing: Нарязване на списъци
Синтаксисът на slicing е: `[x:y:z]` 
- `x` - Начало (включително)
- `y` - Край (без включване)
- `z` - Стъпка на итерация
### Примери:
```python
cute_animals = ['cat', 'raccoon', 'panda', 'red panda', 'marmot']
print(cute_animals[1:3])  # ['raccoon', 'panda']
print(cute_animals[-1])  # 'marmot'
print(cute_animals[1:-1])  # ['raccoon', 'panda', 'red panda']
print(cute_animals[::-1])  # ['marmot', 'red panda', 'panda', 'raccoon', 'cat']
print(cute_animals[-1:0:-1])  # ['marmot', 'red panda', 'panda', 'raccoon']
print(cute_animals[-1:0:-2])  # ['marmot', 'panda']
```
> **[Note]** Когато стъпката е отрицателна, елементите се разместват в обратен ред.
---
## Mutable vs Immutable
- **Mutable (променими)** обекти:
```python
args1 = [9.8, 3.14, 2.71]
args1[1] = 'lorem ipsum'
print(args1)  # [9.8, 'lorem ipsum', 2.71]
```
- **Immutable (непроменими)** обекти:
```python
args2 = (9.8, 3.14, 2.71)
try:
    args2[1] = 'lorem ipsum'
except TypeError as err:
    print(str(err))  # 'tuple' object does not support item assignment
```
