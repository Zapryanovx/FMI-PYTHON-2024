
# Tone, Interval, and Chord Classes

This project defines Python classes to represent musical concepts: tones, intervals, and chords, allowing for the manipulation of musical elements through various operations.

## Tone Class

The `Tone` class represents a musical tone.

### Initialization
```python
c_sharp = Tone("C#")
```

### String Representation
```python
print(str(c_sharp))  # Output: "C#"
```

## Interval Class

The `Interval` class represents an interval, defined by a number of semitones.

### Initialization
```python
number_of_semitones = 3
minor_third = Interval(number_of_semitones)
```

### String Representation
```python
print(str(minor_third))  # Output: "minor 3rd"
```

## Chord Class

The `Chord` class represents a musical chord.

### Initialization
```python
c, d_sharp, g = Tone("C"), Tone("D#"), Tone("G")
c_minor_chord = Chord(c, d_sharp, g)
```

### String Representation
```python
print(str(c_minor_chord))  # Output: "C-D#-G"
```

### Valid Chord Compositions

- Chords must consist of at least 2 unique tones. Creating a `Chord` with only one unique tone raises a `TypeError`.

```python
c = Tone("C")
chord = Chord(c, c)  # Raises TypeError: "Cannot have a chord made of only 1 unique tone"
```

### Chord Qualities

- **Minor Chord**: Contains a "minor 3rd" interval between root and any tone.
- **Major Chord**: Contains a "major 3rd" interval between root and any tone.
- **Power Chord**: Lacks both "minor 3rd" and "major 3rd" intervals.

```python
# Example Usage:
c_minor_chord = Chord(Tone("C"), Tone("D#"), Tone("G"))
print(c_minor_chord.is_minor())  # True

c_major_chord = Chord(Tone("C"), Tone("E"), Tone("G"))
print(c_major_chord.is_major())  # True

c_power_chord = Chord(Tone("C"), Tone("G"))
print(c_power_chord.is_power_chord())  # True
```

## Operations

### Tone and Tone Addition (Returns `Chord`)
```python
c, g = Tone("C"), Tone("G")
result_chord = c + g
print(result_chord)  # Output: "C-G"
```

### Tone and Tone Subtraction (Returns `Interval`)
```python
c, g = Tone("C"), Tone("G")
result_interval = g - c
print(result_interval)  # Output: "perfect 5th"
```

### Tone and Interval Addition (Returns `Tone`)
```python
c = Tone("C")
perfect_fifth = Interval(7)
result_tone = c + perfect_fifth
print(result_tone)  # Output: "G"
```

### Tone and Interval Subtraction (Returns `Tone`)
```python
c = Tone("C")
perfect_fifth = Interval(7)
result_tone = c - perfect_fifth
print(result_tone)  # Output: "F"
```

### Interval and Interval Addition (Returns `Interval`)
```python
perfect_fifth = Interval(7)
minor_third = Interval(3)
result_interval = perfect_fifth + minor_third
print(result_interval)  # Output: "minor 7th"
```

### Chord and Tone Addition (Returns `Chord`)
```python
c5_chord = Chord(Tone("C"), Tone("G"))
result_chord = c5_chord + Tone("E")
print(result_chord)  # Output: "C-E-G"
```

### Chord and Tone Subtraction (Returns `Chord`)
If the resulting chord has fewer than 2 unique tones, raises `TypeError`.

```python
c_major_chord = Chord(Tone("C"), Tone("E"), Tone("G"))
result_chord = c_major_chord - Tone("E")
print(result_chord)  # Output: "C-G"
```

### Chord and Chord Addition (Returns `Chord`)
```python
c5_chord = Chord(Tone("C"), Tone("G"))
this_other_chord = Chord(Tone("A"), Tone("B"))
result_chord = c5_chord + this_other_chord
print(result_chord)  # Output: "C-G-A-B"
```

## Transposing Chords

Use the `Chord.transposed` method to shift all tones in a chord by a given `Interval`.

```python
d_minor_chord = c_minor_chord.transposed(Interval(2))
print(str(d_minor_chord))  # Output: "D-F-A"
```

