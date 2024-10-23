def f1(func):
    def wrapper(n):
        return f'The answer is {func(n)}'
    return wrapper

@f1
def powTwo(n):
    return n ** 2

@f1    
def powThree(n):
    return n ** 3

print(powTwo(2))
print(powTwo(3))

print('----------------------------------------')

def f2(func):
    def wrapper(a, b):
        print(f'a={a}, b={b}')
        sum = a + b
        print(f'sum is calculated...')
        return sum
    return wrapper



print('----------------------------------------')
print('----------------------------------------')
print('----------------------------------------')

def f3(prefix):
    def decorator(func):
        def wrapper(name):
            return f'{prefix}, {func(name)}'
        return wrapper
    return decorator

@f3("Hello")
def getName(name):
    return name

print(getName('Peter'))

print('----------------------------------------')
print('----------------------------------------')
print('----------------------------------------')


def f1(prefix):
    def decorator(func):
        def wrapper(n):
            n+=1
            print(f'{prefix}, {n}', end = ' ')
            return func(n)
        return wrapper
    return decorator

def f2(func):
    def wrapper(n):
        return f'is the new value, {func(n-1)} is the old one'
    return wrapper

@f1('Hello')
@f2
def f3(n):
    return n

print(f3(3))