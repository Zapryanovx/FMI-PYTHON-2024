class Tone:
    """Represent a musical tone."""
    
    TONE_SCALE = ("C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B")
    
    def __init__(self, name):
        self.name = name
        
    def __str__(self):
        return self.name
    
    def __int__(self):
        return Tone.TONE_SCALE.index(self.name)
    
    def __eq__(self, other):
        return self.name == other.name
    
    def __hash__(self):
        """Return a hash value for the Tone object using its name."""
        return hash(self.name)
    
    def __add__(self, other):
        if isinstance(other, Tone):
            return Chord(self, other)
        elif isinstance(other, Interval):
            new_tone_index = Tone.TONE_SCALE.index(self.name) + other.semitone
            return Tone(Tone.TONE_SCALE[new_tone_index % len(Tone.TONE_SCALE)])
        raise TypeError("Invalid operation")
    
    def __radd__(self, other):
        if isinstance(other, Interval):
            raise TypeError("Invalid operation")
    
    def __sub__(self, other):
        if isinstance(other, Tone):
            return Interval((int(self) - int(other)) % len(Tone.TONE_SCALE))
        elif isinstance(other, Interval):
            new_tone_index = Tone.TONE_SCALE.index(self.name) - other.semitone
            return Tone(Tone.TONE_SCALE[new_tone_index % len(Tone.TONE_SCALE)])
        raise TypeError("Invalid operation")
    
    def __rsub__(self, other):
        if isinstance(other, Interval):
            raise TypeError("Invalid operation")


class Interval:
    """Represent a music interval."""
    
    SEMITONE_NAMES = (
        "unison", "minor 2nd", "major 2nd", "minor 3rd", "major 3rd",
        "perfect 4th", "diminished 5th", "perfect 5th", "minor 6th",
        "major 6th", "minor 7th", "major 7th"
    )
    
    def __init__(self, semitone):
        if not isinstance(semitone, int):
            raise TypeError("Invalid semitone")
            
        self.semitone = semitone % len(Interval.SEMITONE_NAMES)
        
    def __str__(self):
        return Interval.SEMITONE_NAMES[self.semitone]
      
    def __neg__(self):
        return Interval(-self.semitone)
    
    def __add__(self, other):
        if isinstance(other, Interval):
            return Interval(self.semitone + other.semitone)
        raise TypeError("Invalid operation")
    
    def __sub__(self, other):
        if isinstance(other, Interval):
            return Interval(self.semitone - other.semitone)
        raise TypeError("Invalid operation")


class Chord:
    """Represent a music chord."""
    
    def __init__(self, *tones):
        
        unique_tones = list(set(tones))
        if len(unique_tones) <= 1:
            raise TypeError("Cannot have a chord made of only 1 unique tone")

        if not all(isinstance(tone, Tone) for tone in unique_tones):
            raise TypeError("Invalid Tone found")
        
        self.root = tones[0]
        self.tones = list(filter(lambda tone: tone != self.root, unique_tones))

    def sort_tones(self):
        """Sort the tones relatively."""
        
        root_index = Tone.TONE_SCALE.index(str(self.root))
        relative_scale = Tone.TONE_SCALE[root_index:] + Tone.TONE_SCALE[:root_index]
        
        return sorted(self.tones, key=lambda tone: relative_scale.index(str(tone)))

    def __str__(self):
        sorted_tones = self.sort_tones()
        return f'{self.root}-{"-".join(map(str, sorted_tones))}'
    
    def find_new_value(self, tone, interval):
        """Set new values after transpose."""
        
        if not isinstance(interval, Interval):
            raise TypeError("Invalid Interval")

        new_tone_index = Tone.TONE_SCALE.index(str(tone)) + interval.semitone
        return Tone(Tone.TONE_SCALE[new_tone_index % len(Tone.TONE_SCALE)])
            
    def transposed(self, interval):
        if not isinstance(interval, Interval):
            raise TypeError("Invalid operation")

        transposed_root = self.find_new_value(self.root, interval)
        transposed_tones = [self.find_new_value(tone, interval) for tone in self.tones]
        
        return Chord(*([transposed_root] + transposed_tones))
        
    def is_minor(self):
        return any(str(tone - self.root) == "minor 3rd" for tone in self.tones)
    
    def is_major(self):
        return any(str(tone - self.root) == "major 3rd" for tone in self.tones)
    
    def is_power_chord(self):
        return not self.is_major() and not self.is_minor()
    
    def __add__(self, other):
        if isinstance(other, Tone):
            return Chord(*([self.root] + self.tones + [other]))
        elif isinstance(other, Chord):
            return Chord(*([self.root] + self.tones + [other.root] + other.tones))
        raise TypeError("Invalid operation")
    
    def __sub__(self, other):
        if isinstance(other, Tone):
            new_tones = [self.root] + self.tones
            if other not in new_tones:
                raise TypeError (f"Cannot remove tone {other} from chord {self}")
            
            new_tones.remove(other)
            return Chord(*new_tones)
        raise TypeError("Invalid operation")
