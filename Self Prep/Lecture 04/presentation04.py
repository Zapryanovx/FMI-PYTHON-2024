#Области на видимост
# > Всяка променлива (име) може да бъде свързана със стойност (binding)
# > Има операции, които променят свързването, например =

global_one = 1
def foo():
    local_one = 2
    print(locals())

print(globals()) # {..., 'global_one': 1}
foo() # {'local_one': 2}

# locals() – връща речник с всички имена в локалната област на видимост
# globals() – връща речник с всички имена в глобалната област на видимост

global_one = 1 #това е глобална променлива
def foo():
    global_one = 2 #това е локална променлива
    print(global_one)
    print(locals())

#двете променливи не са едно и също нещо,
#когато създадем променлива със същото име във вътрешен скоуп се използва тя, ако я достъпим в същия скоуп
#състоянието на едната не влияе на състоянието на другата
foo() #... {'global_one': 2}
print(globals()) #{..., 'global_one': 1, ...}

#подадените аргументи също отиват в locals на функцията
def outer(x):
    print(x)
    def inner():
        x = 0 #ако това го нямаше, долното щеше да изведе празен речник
        print(locals())
    inner()
    print(locals())
    
outer(3)

#Closure
#Closure възниква, когато:
# 1. Имате вложена функция (функция, дефинирана в друга функция).
# 2. Вложената функция използва променливи от външната функция.
# 3. Външната функция връща вложената функция, а нейните променливи продължават да съществуват.

def start(x):
    
    z = 0
    def increment(y):
        print(locals()) 
        return x + y + z

    print(locals())    
    return increment

first_inc = start(0)
print(first_inc(3)) # 3


#[Note] При closure параметрите на обвиващата функция един вид се запомнят и стават част от затвореният контекст на вътрешната,
# затворените променливи от обвиващата функция (x, z) се показват в локалното пространство на имената на вътрешната функция, въпреки че технически те са част от затворения контекст (closure).
# Затворени променливи при closure са тези, които са дефинирани във обвиващата функция и се използват във вътрешната.

#Global vs Nonlocal

#Global
# > Декларира, че дадена променлива се отнася към глобалния обхват (обхватът на модула).
# > Позволява на функцията да чете и модифицира глобална променлива.

#Когато не извършваме манипулация върху глобална променлива, следвайки LEGB правилото, modify_global ще я намери и ще я отпечати
x = 10  # Глобална променлива

def modify_global():
    print(x)
        
modify_global() # 10

#От друга страна, всяка манипулация на променлива третира променливата като локална, т.е.
x = 10  # Глобална променлива

def modify_global():
    try:
        x += 5 #манипулация => търси локална променлива x, а такава няма
    except UnboundLocalError as err:
        print(str(err)) # cannot access local variable 'x' where it is not associated with a value
        
modify_global() # cannot access local variable 'x' where it is not associated with a value

#Този проблем се решава чрез ключовата дума global, което подсказва, че това е глобална променлива
x = 10  # Глобална променлива

def modify_global():
    global x
    x += 5
        
modify_global()
print(x) # 15

#Nonlocal
# > Декларира, че дадена променлива се отнася към обхвата на най-близката обвиваща функция, която не е глобалният обхват.
# > Позволява на вътрешна функция да чете и модифицира променливи от обвиващата функция.

def modify():
    x = 10
    
    def f():
        nonlocal x # без ключовата дума ситуацията става подобна на горния пример (третирането отново е като локална променлива при модификация)
        x += 50
    f()
    print(x)
    
modify() # 60 

def modify():   
    x = 10
    def f():
        def g():
            nonlocal x #най-близкият nonlocal x е този на modify()
            x += 50
        g()
    f()
    print(x)
    
modify() # 60 

def modify():   
    x = 10
    def f():
        x = 30
        def g():
            nonlocal x #най-близкият nonlocal x е този на f()
            x += 50
        g()
        print(x) # 80
    f()
    print(x) # x не се променя, защото вътре сме променили друг x
    
    
modify() # 80 10