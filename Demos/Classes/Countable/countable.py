class Countable:
    
    #protected
    _count = 0
    
    def __init__(self, x):
        self.x = x
        type(self).increase_count()
        
    @classmethod
    def increase_count(cls):
        cls._count += 1
        
    @classmethod
    def decrease_count(cls):
        cls._count -= 1
    
    @classmethod
    def print_count(cls):
        print(cls._count)
            
    def __del__(self):
        type(self).decrease_count()
        

c = Countable(3)
c.print_count()

Countable.print_count()
c.__del__()
Countable.print_count()
print(c.print_count())
