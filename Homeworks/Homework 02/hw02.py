#keys for bushes
bushes_keys = ('храст', 'shrub', 'bush',)

#check if argument is a valid bush
def is_bush(arg):
    if type(arg) != dict or 'name' not in arg:
        return False

    if arg['name'].lower() not in bushes_keys:
        return False

    return True

#check if the multitude of bushes is valid
def is_pretty_bush(price, unique_letters):
    if int(price) == 0:
        return False
    
    return len(unique_letters) % int(price) == 0 and price <= 42.00

def function_that_says_ni(*args, **kwargs):
    
    price = 0.00

    #iterate positioned args
    for positioned in args:
        if is_bush(positioned):
            if 'cost' in positioned:
                price += positioned['cost']
    
    #iterate named args
    for named in kwargs.values():
        if is_bush(named):
            if 'cost' in named:
                price += named['cost']

    #get unique characters found in the bushes in the multitude
    unique_letters = set(''.join([key for key, value in kwargs.items() if is_bush(value)]))

    if is_pretty_bush(price, unique_letters):
        return f'{price:.2f}лв'
    return 'Ni!'
