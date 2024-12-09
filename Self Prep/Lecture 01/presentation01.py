#help() печати документацията на това в скобките (може да се ползва върху всичко, но документацията се крие в docstring-овете)
print(help(5))

def test():
    """eto edin"""
    
    print("""gotin primer""")
    
# help(test) #отпечатва само docstring-овете, които описват функцията, т.е. стоят в началото
             #=> отпечатва само "eto edin"
             
#използва се за извличане на списък с имената на атрибутите и методите, които са достъпни за даден обект 
#[Note] в пайтън всичко е обект
print(dir(5))

#особености при type

#type(<тип>) връща <class 'type'>
print(type(map))
print(type(filter))
print(type(list))

#type(type(<...>)) вложен type винаги връща <class 'type'>
print(type(type("tip")))

print(type((i for i in range(5)))) #<class 'generator'>, тъй като
                                   #се извиква върху обект, чиито тип е генератор
                                   

#можем да сравняваме различни типове числа                  
print(3 < 5.4)

#можем да сравняваме различни стрингове лексикографски                
print("asd" < "asdd")
print("asd" == "asd")

#в пайтън всичко е по референция
a = [1, 2, 3]
b = a
b.append(4)
print(a) # [1, 2, 3, 4]

#колекциите са хетерогенни
my_list = []
my_list.append('word')
my_list.append(5)
my_list.append(False)
print(my_list)

#slicing: [x:y:z] <=> x - начало (включително),
#                     y - край (без елемента на позиция y)
#                     z - стъпка на итерация 

cute_animals = ['cat', 'raccoon', 'panda', 'red panda', 'marmot']

print(cute_animals[1:3]) # ['raccoon', 'panda']
print(cute_animals[-1]) # 'marmot'
print(cute_animals[1:-1]) # ['raccoon', 'panda', 'red panda']
print(cute_animals[::-1]) # ['marmot', 'red panda', 'panda', 'raccoon', 'cat']
print(cute_animals[-1:0:-1]) # ['marmot', 'red panda', 'panda', 'raccoon']
print(cute_animals[-1:0:-2]) # ['marmot', 'panda']

#[Note] елементите се разместват

#Mutable vs immutable
#mutable ~ non-const, можем да ги променяме
args1 = [9.8, 3.14, 2.71]
args1[1] = 'lorem ipsum'
print(args1)

#immutable ~ const, не можем да ги променяме
args2 = (9.8, 3.14, 2.71)

try:
    args2[1] = 'lorem ipsum'
except TypeError as err:
    print(str(err)) # 'tuple' object does not support item assignment
    

    
