import unittest
 
from homework03_vladi import Tone, Interval, Chord
 
 
class TestTone(unittest.TestCase):
    def test_tone_initialization_and_str(self):
        c_sharp = Tone("C#")
        self.assertEqual(str(c_sharp), "C#")
 
    def test_tone_addition_creates_chord(self):
        c = Tone("C")
        g = Tone("G")
        chord = c + g
        self.assertIsInstance(chord, Chord)
        self.assertEqual(str(chord), "C-G")
 
    def test_tone_subtraction_creates_interval(self):
        c = Tone("C")
        f = Tone("F")
        interval = f - c
        self.assertIsInstance(interval, Interval)
        self.assertEqual(str(interval), "perfect 4th")
 
    def test_tone_add_interval_wraps_cyclically(self):
        c = Tone("C")
        interval = Interval(12)
        result_tone = c + interval
        self.assertEqual(str(result_tone), "C")
 
    def test_tone_subtract_interval_wraps_cyclically(self):
        d = Tone("D")
        interval = Interval(14)
        result_tone = d - interval
        self.assertEqual(str(result_tone), "C")
 
    def test_tone_add_zero_interval(self):
        c = Tone("C")
        zero_interval = Interval(0)
        result_tone = c + zero_interval
        self.assertEqual(str(result_tone), "C")
 
    def test_tone_add_large_interval(self):
        c = Tone("C")
        large_interval = Interval(24)
        result_tone = c + large_interval
        self.assertEqual(str(result_tone), "C")
 
 
class TestInterval(unittest.TestCase):
    def test_interval_initialization_and_str(self):
        interval = Interval(3)
        self.assertEqual(str(interval), "minor 3rd")
 
    def test_interval_cyclic_behavior(self):
        interval = Interval(13)
        self.assertEqual(str(interval), "minor 2nd")
 
    def test_interval_addition(self):
        minor_third = Interval(3)
        major_sixth = Interval(9)
        result_interval = minor_third + major_sixth
        self.assertEqual(str(result_interval), "unison")
        
    def test_interval_large_addition(self):
        interval1 = Interval(15) 
        interval2 = Interval(13)  
        result_interval = interval1 + interval2
        self.assertEqual(str(result_interval), "major 3rd") 
 
 
class TestChord(unittest.TestCase):
    def test_chord_initialization_and_str(self):
        c = Tone("C")
        e = Tone("E")
        g = Tone("G")
        chord = Chord(c, e, g)
        self.assertEqual(str(chord), "C-E-G")
 
    def test_chord_with_duplicate_tones(self):
        c = Tone("C")
        another_c = Tone("C")
        g = Tone("G")
        chord = Chord(c, another_c, g)
        self.assertEqual(str(chord), "C-G")
 
    def test_chord_with_single_unique_tone_raises_error(self):
        c = Tone("C")
        another_c = Tone("C")
        with self.assertRaises(TypeError) as e:
            Chord(c, another_c)
        self.assertEqual(str(e.exception), "Cannot have a chord made of only 1 unique tone")
 
    def test_chord_with_single_tone_and_addition_of_duplicate(self):
        c = Tone("C")
        with self.assertRaises(TypeError) as e:
            Chord(c, c)
        self.assertEqual(str(e.exception), "Cannot have a chord made of only 1 unique tone")
 
    def test_chord_is_minor(self):
        c = Tone("C")
        d_sharp = Tone("D#")
        g = Tone("G")
        chord = Chord(c, d_sharp, g)
        self.assertTrue(chord.is_minor())
 
    def test_chord_is_not_minor(self):
        c = Tone("C")
        d = Tone("D")
        g = Tone("G")
        chord = Chord(c, d, g)
        self.assertFalse(chord.is_minor())
 
    def test_chord_is_major(self):
        c = Tone("C")
        e = Tone("E")
        g = Tone("G")
        chord = Chord(c, e, g)
        self.assertTrue(chord.is_major())
 
    def test_chord_is_not_major(self):
        c = Tone("C")
        f = Tone("F")
        g = Tone("G")
        chord = Chord(c, f, g)
        self.assertFalse(chord.is_major())
 
    def test_chord_is_power_chord(self):
        c = Tone("C")
        g = Tone("G")
        f = Tone("F")
        chord = Chord(c, f, g)
        self.assertTrue(chord.is_power_chord())
 
    def test_chord_not_power_due_to_minor_third(self):
        c = Tone("C")
        d_sharp = Tone("D#")
        g = Tone("G")
        chord = Chord(c, d_sharp, g)
        self.assertFalse(chord.is_power_chord())
 
    def test_chord_add_tone_creates_new_chord(self):
        c5_chord = Chord(Tone("C"), Tone("G"))
        result_chord = c5_chord + Tone("E")
        self.assertEqual(str(result_chord), "C-E-G")
 
    def test_chord_remove_tone_reduces_chord(self):
        c_major = Chord(Tone("C"), Tone("E"), Tone("G"))
        result_chord = c_major - Tone("E")
        self.assertEqual(str(result_chord), "C-G")
 
    def test_chord_remove_last_tone_raises_error(self):
        c5 = Chord(Tone("C"), Tone("G"))
        with self.assertRaises(TypeError) as e:
            c5 - Tone("G")
        self.assertEqual(str(e.exception), "Cannot have a chord made of only 1 unique tone")
 
    def test_chord_remove_nonexistent_tone_raises_error(self):
        c5 = Chord(Tone("C"), Tone("G"))
        with self.assertRaises(TypeError) as e:
            c5 - Tone("A")
        self.assertEqual(str(e.exception), "Cannot remove tone A from chord C-G")
 
    def test_chord_add_chord_combines_tones(self):
        c5 = Chord(Tone("C"), Tone("G"))
        another_chord = Chord(Tone("D"), Tone("F"))
        result_chord = c5 + another_chord
        self.assertEqual(str(result_chord), "C-D-F-G")
 
    def test_chord_transposed_upwards(self):
        c_minor = Chord(Tone("C"), Tone("D#"), Tone("G"))
        transposed_chord = c_minor.transposed(Interval(2))
        self.assertEqual(str(transposed_chord), "D-F-A")
 
    def test_chord_transposed_downwards(self):
        d_major = Chord(Tone("D"), Tone("F#"), Tone("A"))
        transposed_chord = d_major.transposed(Interval(-2))
        self.assertEqual(str(transposed_chord), "C-E-G")
 
    def test_chord_add_existing_tone(self):
        c = Tone("C")
        g = Tone("G")
        chord = Chord(c, g)
        new_chord = chord + Tone("G")
        self.assertEqual(str(new_chord), "C-G")
 
    def test_chord_remove_nonexistent_tone_error_message(self):
        chord = Chord(Tone("C"), Tone("G"))
        with self.assertRaises(TypeError) as e:
            chord - Tone("A")
        self.assertEqual(str(e.exception), "Cannot remove tone A from chord C-G")
 
    def test_chord_transpose_negative_interval(self):
        chord = Chord(Tone("D"), Tone("F#"), Tone("A"))
        transposed_chord = chord.transposed(Interval(-14))
        self.assertEqual(str(transposed_chord), "C-E-G")
 
 
if __name__ == "__main__":
    unittest.main()