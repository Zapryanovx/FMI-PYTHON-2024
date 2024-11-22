# Интродукция
Тъй като нямате търпение да разберете резултатите си от първото контролно, даваме ви възможността да го направите по-рано от предвиденото.
Който успее да отключи ключалката, ще види резултатите си в лога от изпълнението на тестовете си, когато крайният срок за предизвикателството приключи.
Пък и ще получиш точка за правилно решено предизвикателство.

### Какво да напишете
Напишете клас `LockPicker_<ФН>`, където "<ФН>" е заменено от вашия ФН.
Класът трябва да очаква един позиционен аргумент при инициализация. Аргументът е обект, който представлява ключалка за отключване.
Класът ви трябва да има публичен метод `unlock`, който да отключва ключалката при едно извикване, т.е. от първия път.

```python
# lock е някакъв обект, за който пише по-долу
lock_picker = LockPicker_FN1234(lock)
lock_picker.unlock()
```

### Какво да очаквате
Обектът, който подаваме, т.е. ключалката, е абсолютна мистерия за вас, но той има механизъм, с който да ви помогне да се справите.

Обектът има публичен метод `pick`.
Извиквайки този метод, можете да се опитате да отключите ключалката.
Методът получава произволен брой позиционни аргументи. Не очаква именувани.

Ако аргументите, подадени на `pick`, са точно тези, които ключалката очаква (правилния тип, правилната стойност и правилния ред), то ключалката се отключва и методът `pick` връща `True`.

Ако обаче това не се случи, методът ще хвърли грешки, които да ви помогнат да се поправите. Грешките, които можете да очаквате, са варианти на `TypeError` и `ValueError`, но подобрени.
Разбирайте - наследили сме тези две вградени изключения и сме ги подобрили. Това го казваме, за да ви е ясно, че не можете да сравнявате типа на получената грешка директно с `TypeError` или `ValueError`, използвайки `type(ex) is TypeError`, защото типът им няма да е такъв, а просто ще го наследява.

Всяка една от нашите грешки ще има две допълнителни полета с информация, полезна за вас:
- **position**
- **expected**

Стойността на тези полета можете да вземете от грешката, която се е възбудила.

```python
try:
    lock.pick()
except Exception as ex:
    print(ex.position)
    print(ex.expected)
```

### Ето и кога какви грешки ще видите
Грешките са подредени по приоритет.
Ако имате няколко грешки, ще се възбуди първата намерена в този списък (от горе надолу).

1. Ако броят аргументи, подадени на `pick`, не съвпада с очаквания брой, ще получите `TypeError`.
   - Специалните полета в грешката ще са:
     - **position**: `None`
     - **expected**: `int`, който показва броя очаквани аргументи

2. Ако някой аргумент, подаден на `pick`, не е от очаквания тип, ще получите `TypeError`.
   - Специалните полета в грешката ще са:
     - **position**: `int`, който показва позицията на грешния аргумент, в списъка подадени аргументи, ЗАПОЧВАЩА ОТ 1
     - **expected**: `type`, който показва типът, който се очаква на тази позиция

3. Ако някой аргумент, подаден на `pick`, не е с очакваната стойност, ще получите `ValueError`.
   - Специалните полета в грешката ще са:
     - **position**: `int`, който показва позицията на грешния аргумент, в списъка подадени аргументи, ЗАПОЧВАЩА ОТ 1
     - **expected**: очакваната стойност на тази позиция

### Пример

```python
# lock е някаква ключалка, а аргументите, които `pick` очаква за отключване, са (1, 'две')
lock.pick()  # TypeError, в който position=None и expected=2
lock.pick([], None)  # TypeError, в който position=1 и expected=int
lock.pick(1, 'two')  # ValueError, в който position=2 и expected='две'
```

### Аутро
Дори случайно да не си бил на контролно, ако си записан в курса, пак можеш да се бориш за точка.
Използваме ФН, който използвате в сайта на курса. Имаше колеги с няколко ФН номера - използвайте този, който намирате в профила си тук.
Обектите, които `pick` очаква, ще са само от вградени типове, с които сте запознати от лекциите. Няма да тестваме с нищо екзотично.
Разбираме, че има опасност да започнете да брутфорсвате, затова решенията ви ще трябва да се справят с проблема за не повече от 1 секунда, което ще е напълно достатъчно, ако имате адекватен алгоритъм.