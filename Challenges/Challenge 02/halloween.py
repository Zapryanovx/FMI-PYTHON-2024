class HauntedMansion:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __getattribute__(self, name):
        PREFIX = "spooky_"
        if name.startswith(PREFIX):
            return object.__getattribute__(self, name.removeprefix(PREFIX))
        elif name.startswith("__") and name.endswith("__"):
            return object.__getattribute__(self, name)
        else:
            return "Booooo, only ghosts here!"
