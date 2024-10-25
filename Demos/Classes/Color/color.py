class Color:
    def __init__(self, rgba):
        self._rgba = tuple(rgba)
        
    @property
    def rgba(self):
        return self._rgba
    
    @rgba.setter
    def rgba(self, value):
        self._rgba = tuple(value)
        
color = Color([1, 2, 3])
print(color.rgba)
color.rgba = [3, 2, 1]
print(color.rgba)

setattr(color, 'rgba', [10, 11, 12])
print(color.rgba)
print(getattr(color, 'rgba'))
