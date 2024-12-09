
#Какъв ще е резултатът от следните операции?

print(3 / 2)  # 1.5
print(3 // 2)  # 1
print(0.1 + 0.2)  # 0.30000000000000004
print(0.1 + 0.1)  # 0.2
print(0.5 - 0.2)  # 0.3
print(0.3 / 3)  # 0.09999999999999999

#[Note] Важно е да се отбележи, че има особености при дробните числа поради
#представянето им в паметта (представят се в двоичен формат вместо десетичен и някои такива не могат да бъдат точно представени)

#Какъв е типът?
things = ['eggs', ('spam', 'spam', 'spam'), 'ham']
print(type(things[1][2][3])) # <class 'str'>
print(things[1][2][3]) # 'm'
#В пайтън няма тип char, има само str (низ)

things = ['eggs', ('spam', 'spam', 'spam'), 'ham']
try:
    things[1][2][3] = 'h'
except TypeError as err:
    print(str(err)) # 'str' object does not support item assignment

#низовете също са immutable    
print(type(things[1][2][3])) # <class 'str'>

#също така
things[1] = 'ham' #листа е mutable
print(things) # ['eggs', 'ham', 'ham'] 

things[1] = ('spam', 'spam', 'spam') #ако не го върнем към началното състояние, отново ще имаме случая, в който не можем да променим string
                                     #защото отдолу things[1][2] ще ни стане буквата 'а'
try:
    things[1][2] = 'ham' #things[1] е tuple (immutable) => не можем да променин негов елемент 
except TypeError as err:
    print(str(err)) # 'tuple' object does not support item assignment

# is vs ==
# > is - проверява дали е една и съща инстанция
# > == - проверява дали СЪДЪРЖАНИЕТО на двете инстанции е едно и също (може двете инстанции да са една)

a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b) #съдържанието на a и b е едно и също
print(a is b) #въпреки това са два различни обекта
print(a == c) #съдържанието на a и c е едно и също
print(a is c) #казахме, че в пайтън всичко е по референция => а и c са една и съща инстанция

#True
#False
#True
#True

#Списъците съдържат "референции" към елементи.
coffee, cheese, crackers, tea = 'coffee', 'cheese', 'crackers', 'tea'

#unpacking
things_i_like = [coffee, cheese, crackers]
things_you_like = [crackers, coffee, tea]

print(things_i_like[0] == things_you_like[1]) # съдържанието е едно и също => True
print(things_i_like[0] is things_you_like[1]) # и двете сочат към едно и също нещо => True

things_i_like[0] = 'kafe' #това пренасочва референцията на първата клетка към 'kafe', не променя обекта coffee

print(things_i_like[0] == things_you_like[1]) # съдържанието вече не е едно и също => False
print(things_i_like[0] is things_you_like[1]) # вече сочат към различни неща => False

#Също така
coffee, cheese, crackers, tea = 'coffee', 'cheese', 'crackers', 'tea'

things_i_like = [coffee, cheese, crackers]
things_you_like = [crackers, coffee, tea]

print(things_i_like[0] == things_you_like[1]) # съдържанието е едно и също => True
print(things_i_like[0] is things_you_like[1]) # и двете сочат към едно и също нещо => True

things_i_like[0] = 'coffee' #това пренасочва референцията на първата клетка към 'coffee', не променя обекта coffee

print(things_i_like[0] == things_you_like[1]) # съдържанието е едно и също => True
print(things_i_like[0] is things_you_like[1]) # и двете сочат към едно и също нещо ('coffee') => True

#Списък с референция към себе си

cheeses = ['brie', 'bergkäse', 'kashkaval', 'leipäjuusto']
cheeses.append(cheeses)
cheeses[-1] is cheeses # True
print(cheeses) # ['brie', 'bergkäse', 'kashkaval', 'leipäjuusto', [...]]

#Листът cheeses има референция към себе си на позиция 4, тоест на това място се получава бездънна рекурсия
print(cheeses[4][4][4][4][4][4][4][4][4][4][0]) # brie

#Съответно, ако заменим елемента на позиция 4 някъде навътре, то тя ще се прекрати, тъй като е референция, т.е.
cheeses[4][4][4][4][4][4][4][4][4][4] = 'neshto'
print(cheeses) #['brie', 'bergkäse', 'kashkaval', 'leipäjuusto', 'neshto']

try:
    cheeses[4][4][4][4][4][4][4][4][4][4] = 'neshto' #рекурсията е прекъсната и вече не можем да влизаме колкото си искаме навътре
except IndexError as err:
    print(str(err)) # string index out of range
    
#Unpacking
(a, b) = 1, 2
print(a) # 1

a, b = 1, 2
print(a) # 1

numbers = (1, 2, 3)
a, b, c = numbers
print(a) # 1

a, *b, c = 1, 2, 3, 4, 5
print(a) # 1
print(b) # [2, 3, 4] (b е длъжно да вземе всичко измежду a и c, тоест първия и последния)
print(c) # 5

# *b, сигнализира, че b ще разопакова символите между a и c, т.е. това няма да е валидно,
#тъй като очаква да са равен брой аргументи вляво и вдясно

try:
    a, b, c = 1, 2, 3, 4, 5
except ValueError as err:
    print(str(err)) # too many values to unpack (expected 3)


#Не можем да сравняваме tuple и list
try:
    print((1, 2) < [1, 2])
except TypeError as err:
    print(str(err)) # string index out of range


