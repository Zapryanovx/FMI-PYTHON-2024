class Limb:
    name = 'Limb'

    def introduce(self):
        return f"I am a {self.name}"
    
class Hand(Limb):
    
    name = 'Hand'
    def introduce(self):
        return f"I am THE {self.name}"

hand = Hand()
print(hand.introduce()) 

print(Hand.__dict__)
Hand = type('Hand',
    (Limb, ),
    {
    'name': 'hand',
    'say_hi': lambda self: print(f"Hi. I am a {self.name}.")
    }
)

hand = Hand()
print(hand.name)