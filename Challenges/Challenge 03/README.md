# ProtectedSection Контекстен Мениджър

### Обща информация

Ние не сме безгрешни, и вероятно и вие не сте. Но сме истински! Въпреки това искаме да дефинираме контекстен мениджър, който ни позволява да изпълняваме (относително) безгрешен блок от код.

### Описание

`ProtectedSection` е контекстен мениджър, който приема два опционални параметъра - `log` и `suppress`. И двата параметъра приемат като стойност tuple от изключения.

Целта е да се обработват изключения в блока на контекста, като те или се логват, или се подтискат, без да спират изпълнението на програмата.

#### Параметри
- **log**: Tuple от изключения, които трябва да бъдат логнати.
- **suppress**: Tuple от изключения, които трябва да бъдат подтиснати (без да се логват).

### Поведение

- Ако възникне грешка в блока на контекста, която съответства на изключение в `log`, тя трябва да бъде логната (т.е. запазена) и да не прекъсва изпълнението на програмата.
- Ако грешката съответства на изключение в `suppress`, тя трябва да бъде подтисната, без да се логва.
- Ако един и същ тип изключение е включен както в `log`, така и в `suppress`, ще се даде приоритет на логването.

### Примери за използване

По-долу са показани примери за използване на контекстния мениджър `ProtectedSection` и очакваното поведение в различни ситуации.

#### Пример 1: Логване на изключение

```python
with ProtectedSection(log=(ZeroDivisionError, IndexError)) as err:
    x = 1 / 0

print(err.exception)
# division by zero
print(type(err.exception))
# <class 'ZeroDivisionError'>
```
В този пример `ZeroDivisionError` се логва. Обектът `err.exception` съдържа реалното изключение (`ZeroDivisionError`), а не само текстово представяне.

#### Пример 2: Подтискане на изключение

```python
with ProtectedSection(suppress=(ZeroDivisionError, IndexError)) as err:
    x = 1 / 0

print(err.exception)
# None
```
В този случай `ZeroDivisionError` е подтиснат и `err.exception` е `None`, тъй като изключението не е логнато.

#### Пример 3: Използване на `log` и `suppress` заедно

```python
with ProtectedSection(log=(ZeroDivisionError, IndexError), suppress=(TypeError, ZeroDivisionError, Exception)) as err:
    x = 1 / 0

print(err.exception)
# division by zero
print(type(err.exception))
# <class 'ZeroDivisionError'>
```
Тук и двата параметъра `log` и `suppress` са използвани, но се дава приоритет на логването на `ZeroDivisionError`.
