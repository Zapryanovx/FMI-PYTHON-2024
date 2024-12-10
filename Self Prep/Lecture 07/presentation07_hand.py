class Hand:
    def __init__(self):
        self.thumb = 'Палец'
        self.index_finger = 'Показалец'
        self.middle_finger = 'Среден'
        self.ring_finger = 'Безименен'
        self.pinkie = 'Кутре'
        
    #__getitem__(self, index):
    #позволява ни достъп чрез индексация на член-данните (и се извиква чрез опит за достъпване на атрибут чрез [])
    
    def __getitem__(self, index):
        return (self.thumb, self.index_finger, self.middle_finger,
                self.ring_finger, self.pinkie)[index]

hand = Hand()
print(hand[4]) # Кутре

#Какво ще се случи тук?
hand = Hand()
try:
    hand[2] = 'кебапче'
except TypeError as err:
    print(str(err)) # 'Hand' object does not support item assignment
    
#__getitem__ ни дава само достъпване на атрибутите, но не ни позволява и да ги променяме,
#ако искаме да ги променим трябва да използваме __setitem__

class Hand:
    def __init__(self):
        self.thumb = 'Палец'
        self.index_finger = 'Показалец'
        self.middle_finger = 'Среден'
        self.ring_finger = 'Безименен'
        self.pinkie = 'Кутре'
        
    #__getitem__(self, index):
    #позволява ни достъп чрез индексация на член-данните (и се извиква чрез опит за достъпване на атрибут чрез [])
    
    def __getitem__(self, index):
        return (self.thumb, self.index_finger, self.middle_finger,
                self.ring_finger, self.pinkie)[index]
    
    #__setitem__(self, index, val)
    #използва се за задаване на стойности за елементи на обект чрез индексиране със знак за присвояване ([] =)

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
print(hand.index_finger) # 'кебапче'

#Какво ще се случи тук?
hand = Hand()
try:
    getattr(hand, 'test')
except AttributeError as err:
    print(str(err)) # 'Hand' object has no attribute 'test'
    
#Тоест, ако пръста е невалиден, кодът хвърля грешка
#Ако не желаем това поведение може да използваме __getattr__(self, name)

class Hand:
    def __init__(self):
        self.thumb = 'Палец'
        self.index_finger = 'Показалец'
        self.middle_finger = 'Среден'
        self.ring_finger = 'Безименен'
        self.pinkie = 'Кутре'
        
    #__getitem__(self, index):
    #позволява ни достъп чрез индексация на член-данните (и се извиква чрез опит за достъпване на атрибут чрез [])
    
    def __getitem__(self, index):
        return (self.thumb, self.index_finger, self.middle_finger,
                self.ring_finger, self.pinkie)[index]
    
    #__setitem__(self, index, val)
    #използва се за задаване на стойности за елементи на обект чрез индексиране със знак за присвояване ([] =)

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
    
    #__getattr__ e механизъм, който ще се изпълни само ако търсен атрибут го няма,
    #което решава проблема с хвърлянето на грешка, ако не го желаем
    
    def __getattr__(self, name):
        return f"Това е ръка v1.0. Все още няма {name} :("
    
hand = Hand()
print(hand.middle_finger) # Среден
print(hand.sixth_finger) # Това е ръка v1.0. Все още няма sixth_finger :(
    
#Какво ще се случи тук?
hand = Hand()

hand.pinkie = 'test' #това извиква __setattr__(self, name, value)
print(hand.pinkie)

class Hand:
    def __init__(self):
        self.thumb = 'Палец'
        self.index_finger = 'Показалец'
        self.middle_finger = 'Среден'
        self.ring_finger = 'Безименен'
        self.pinkie = 'Кутре'
        
    #__getitem__(self, index):
    #позволява ни достъп чрез индексация на член-данните (и се извиква чрез опит за достъпване на атрибут чрез [])
    
    def __getitem__(self, index):
        return (self.thumb, self.index_finger, self.middle_finger,
                self.ring_finger, self.pinkie)[index]
    
    #__setitem__(self, index, val)
    #използва се за задаване на стойности за елементи на обект чрез индексиране със знак за присвояване ([] =)

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
    
    #__getattr__ e механизъм, който ще се изпълни само ако търсен атрибут го няма,
    #което решава проблема с хвърлянето на грешка, ако не го желаем
    
    def __getattr__(self, name):
        return f"Това е ръка v1.0. Все още няма {name} :("
    
    #__setattr__ се извиква винаги при присвояване на нова стойност на член-данна,
    #това значи, че ако в тялото му има просто self.name = value, това отново ще извика същия метод
    #и ще се получи бездънна рекурсия, затова използваме __setattr__ на Базовия пайтън клас (object)
    
    def __setattr__(self, name, value):
        print(f"Нова стойност за {name} - {value}")
        object.__setattr__(self, name, value)
        
    def f():
        print("f")
    
def g():
    print("g")
        
print()        
hand = Hand()
hand.pinkie = 'test'
print(hand.pinkie)

hand.f = g # извиква се и при промяна на методи
hand.f() # g

#Можем да искаме да имаме различно поведение, при достъпване,
#което не се извиква само когато атрибута или метода го няма

class Hand:
    
    prust = 'asd'
    
    def __init__(self):
        self.thumb = 'Палец'
        self.index_finger = 'Показалец'
        self.middle_finger = 'Среден'
        self.ring_finger = 'Безименен'
        self.pinkie = 'Кутре'
        
    #__getitem__(self, index):
    #позволява ни достъп чрез индексация на член-данните (и се извиква чрез опит за достъпване на атрибут чрез [])
    
    def __getitem__(self, index):
        return (self.thumb, self.index_finger, self.middle_finger,
                self.ring_finger, self.pinkie)[index]
    
    #__setitem__(self, index, val)
    #използва се за задаване на стойности за елементи на обект чрез индексиране със знак за присвояване ([] =)

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
    
    #__getattr__ e механизъм, който ще се изпълни само ако търсен атрибут го няма,
    #което решава проблема с хвърлянето на грешка, ако не го желаем
    
    def __getattr__(self, name):
        return f"Това е ръка v1.0. Все още няма {name} :("
    
    #__setattr__ се извиква винаги при присвояване на нова стойност на член-данна,
    #това значи, че ако в тялото му има просто self.name = value, това отново ще извика същия метод
    #и ще се получи бездънна рекурсия, затова използваме __setattr__ на Базовия пайтън клас (object)
    
    def __setattr__(self, name, value):
        print(f"Нова стойност за {name} - {value}")
        object.__setattr__(self, name, value)
        
    #__getattribute__(self, name) се извиква абсолютно винаги при търсене, ако не го намери се извиква __getattr__,
    #подобно на __setattr__ може да доведе до бездънна рекурсия
    def __getattribute__(self, name):
        print(f"Някой ми бърка по пръстите и иска {name}")
        return object.__getattribute__(self, name)
    
hand = Hand()
print(hand.pinkie)
print(hand.sixth_finger)

hand = Hand()
print(hand.__dict__) #__dict__ е речник, който съдържа всички атрибути на обекта.
print(hand.__class__) #__class__ е атрибут, който сочи към класа, към който принадлежи даден обект. С него можете да разберете типа на обекта и да получите достъп до класа му.

print(Hand.__dict__) 

#накратко hand.__dict__ Върху инстанция - всичко в __init__
#Hand.__dict__ - всичко останало