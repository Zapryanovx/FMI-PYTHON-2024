lectures_location = {'Tuesday': '101', 'Thursday': '200'}

lectures_location['Friday'] = '204' #можем да създаваме нови ключове
print(lectures_location) # {'Tuesday': '101', 'Thursday': '200', 'Friday': '204'}


lectures_location['Friday'] = '205' #да променяме стойностите им
print(lectures_location) # {'Tuesday': '101', 'Thursday': '200', 'Friday': '205'}


try: 
    lectures_location['Wednesday'] # но и не да достъпваме такива, които ги няма
except KeyError as err:
    print(type(err), str(err)) # <class 'KeyError'> 'Wednesday'
    

#ако имаме несъществуващ ключ
print(lectures_location.get('Wednesday', 'няма сряда')) #няма сряда (търси подаден ключ в речника,  
                                                        # ако го няма връща втория подаден агрумент, ако го има - стойността зад ключа)
print(lectures_location.get('Friday', 'няма сряда')) # 205


#Какъв ще е резултатът от следния код?
other_things = (42, [1, 2, 3], 'baba')

try:
    other_things[1] += [4] #това се раздробява на other_things[1] = other_things[1] + [4]
                           #поради редът на действие първо ще се добави [4] към other_things[1]
                           #когато стигнем до знака за присвояване, това ще хвърли грешка, тъй като tuple e immutable колекция
except TypeError as err:
    print(str(err)) # 'tuple' object does not support item assignment

print(other_things) #(42, [1, 2, 3, 4], 'baba') - макар и грешката, кортежа все пак е променен

#Print
main_character = "Captain Jack Sparrow"
print(f"This is the tale of {main_character}") # "This is the tale of Captain Jack Sparrow"

#Има и интересни опции за форматиране:
heights = {"Mount Everest": 8849, "Musala": 2925, "Shaq": 2.16}
for name, height in heights.items():
    print(f"{name:15} ==> {height:10}") 

# "Mount Everest ==> 8849"
# "Musala ==> 2925"
# "Shaq ==> 2.16"

#15 в {name:15}
#Резервира 15 символа за текста, представен от променливата name.
#Ако текстът е по-къс от 15 символа: Той ще бъде допълнен с интервали отдясно (по подразбиране).
#Ако текстът е по-дълъг от 15 символа: Той няма да бъде съкратен – ще заеме толкова място, колкото е нужно.

#10 в {height:10}
#Резервира 10 символа за числото, представено от променливата height.
#Ако числото е по-кратко: То ще бъде допълнено с интервали отляво (за да се изравнят стойностите).
#Ако числото е по-дълго: Няма да бъде съкратено.

#[Note] Подравняването зависи от типа на променливата
# - Текстът се подравнява наляво. (колекциите се третират като текст)
# - Числата се подравняват надясно.

# В контекста на булевите операции като лъжа се интерпретират следните стойности:
#     > False
#     > None
#     > числото 0 независимо от типа числа (например 0, 0.0, 0j)
#     > празният низ
#     > празни контейнери (tuple, list, dict, set)
#     > наши типове могат да дефинират как да бъдат оценявани като булеви променливи
# Всички останали стойности се интерпретират като истина.

#str() прехвърля всичко в текст
b = 10
print(str(b)) # '10'

nums = (1, 2, 3)
nums = list(nums)
nums # [1, 2, 3]
print(str(['baba', 2])) # "['baba', 2]" 

#match case
http_status = 400
match http_status:
    case 400:
        print("Bad request") #Bad request
    case 401 | 403: # 401 OR 403
        print("Authentication error")
    case 404:
        print("Not found")
    case _: # default
        print("Other error")


#В пайтън switch-case == match-case, а или в условията за match вместо or е побитово |

def f(a=5, b=10, c=15):
    print(c)
    
f(c=200, a=5.243, b=-1)