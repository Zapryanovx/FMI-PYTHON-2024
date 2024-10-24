import unittest
from io import StringIO
import sys
from abomination_decorator import type_check

@type_check("in")(int, float, complex)
@type_check("out")(int, float, complex)
def power(num, power):
    return num ** power

@type_check("in")(int, float, complex)
@type_check("out")(int, float, complex)
def power_invalid_output(num, power):
    return set([num ** power])

@type_check("in")(str)
@type_check("out")(str)
def concatenate(*strings, separator=' beep boop '):
    return separator.join(strings)

@type_check("in")(int)
@type_check("out")(int)
def increment(num):
    return num + 1

@type_check("in")(list)
@type_check("out")(list)
def reverse_list(arr):
    return arr[::-1]

@type_check("in")(dict)
@type_check("out")(int)
def dict_length(test):
    return len(test)

@type_check("in")(str, int)
@type_check("out")(str)
def repeat_string(string, times):
    return string * times

@type_check("in")(str, int)
@type_check("out")(str)
def repeat_string_wrong_return(string, times):
    return [string * times]

@type_check("in")(int, str)
def test_func_kwarg(a, b, **kwargs):
    return f"{a} {b} {kwargs.get('extra', '')}"

@type_check("in")(str)
def concatenate_all(*strings):
    return ' '.join(strings)

@type_check("out")(str)
def return_wrong_structure():
    return ["this", "should", "be", "a", "string"]

@type_check("in")(str)
def none_check(value):
    return value

@type_check("in")(int, str)
def test_func_combined_args(a, b, c="default"):
    return f"{a} {b} {c}"

class TestTypeCheckDecorator(unittest.TestCase):

    def setUp(self):
        self.held_stdout = StringIO()
        sys.stdout = self.held_stdout

    def tearDown(self):
        sys.stdout = sys.__stdout__

    def test_invalid_input_arguments(self):
        result = power(6j, 2)
        output = self.held_stdout.getvalue().strip()
        self.assertEqual((-36+0j), result)

    def test_invalid_output_value(self):
        result = power_invalid_output(2, 2)
        output = self.held_stdout.getvalue().strip()

        self.assertIn("Invalid output value, expected <class 'int'>, <class 'float'>, <class 'complex'>!", output)
        self.assertEqual({4}, result)

    def test_concatenate_invalid_input(self):
        with self.assertRaises(TypeError):
            concatenate(5, '6')

        output = self.held_stdout.getvalue().strip()
        self.assertIn("Invalid input arguments, expected <class 'str'>!", output)

    def test_concatenate_valid(self):
        result = concatenate('Hello', 'World')
        output = self.held_stdout.getvalue().strip()

        self.assertEqual("", output)
        self.assertEqual("Hello beep boop World", result)

    def test_increment_valid(self):
        result = increment(5)
        output = self.held_stdout.getvalue().strip()

        self.assertEqual("", output)
        self.assertEqual(6, result)

    def test_increment_invalid_input(self):
        with self.assertRaises(TypeError):
            increment('5')

        output = self.held_stdout.getvalue().strip()
        self.assertIn("Invalid input arguments, expected <class 'int'>!", output)

    def test_reverse_list_valid(self):
        result = reverse_list([1, 2, 3])
        output = self.held_stdout.getvalue().strip()

        self.assertEqual("", output)
        self.assertEqual([3, 2, 1], result)

    def test_reverse_list_invalid_input(self):
        with self.assertRaises(TypeError):
            reverse_list(123)

        output = self.held_stdout.getvalue().strip()
        self.assertIn("Invalid input arguments, expected <class 'list'>!", output)

    def test_dict_length_valid(self):
        result = dict_length({'a': 1, 'b': 2})
        output = self.held_stdout.getvalue().strip()

        self.assertEqual("", output)
        self.assertEqual(2, result)

    def test_dict_length_invalid_output(self):
        result = dict_length([])

        output = self.held_stdout.getvalue().strip()
        self.assertIn("Invalid input arguments, expected <class 'dict'>!", output)

    def test_repeat_string_valid(self):
        result = repeat_string('Hello', 3)
        output = self.held_stdout.getvalue().strip()

        self.assertEqual("", output)
        self.assertEqual('HelloHelloHello', result)

    def test_repeat_string_invalid_input(self):
        with self.assertRaises(TypeError):
            repeat_string('Hello', '3')

        output = self.held_stdout.getvalue().strip()
        self.assertIn("", output)

    def test_repeat_string_invalid_output(self):
        result = repeat_string_wrong_return('Hello', 3)
        output = self.held_stdout.getvalue().strip()

        self.assertIn("Invalid output value, expected <class 'str'>!", output)

    def test_mixed_valid_invalid_input(self):
        with self.assertRaises(TypeError):
            concatenate('Hello', 123, 'World')
        output = self.held_stdout.getvalue().strip()
        self.assertIn("Invalid input arguments, expected <class 'str'>!", output)

    def test_with_kwargs(self):
        result = test_func_kwarg(1, "test", extra="additional")
        output = self.held_stdout.getvalue().strip()
        self.assertEqual("", output)
        self.assertEqual(result, "1 test additional")

    def test_invalid_kwargs(self):
        res = test_func_kwarg(1, [3,4,5], extra="additional")
        output = self.held_stdout.getvalue().strip()
        self.assertIn("Invalid input arguments, expected <class 'int'>, <class 'str'>!", output)

    def test_var_args_valid(self):
        result = concatenate_all('Hello', 'beautiful', 'world')
        output = self.held_stdout.getvalue().strip()
        self.assertEqual("", output)
        self.assertEqual(result, 'Hello beautiful world')

    def test_var_args_invalid(self):
        with self.assertRaises(TypeError):
            concatenate_all('Hello', 'world', 42)
        output = self.held_stdout.getvalue().strip()
        self.assertIn("Invalid input arguments, expected <class 'str'>!", output)

    def test_empty_string(self):
        result = concatenate('', '')
        output = self.held_stdout.getvalue().strip()
        self.assertEqual("", output)
        self.assertEqual(result, " beep boop ")

    def test_empty_list(self):
        result = reverse_list([])
        output = self.held_stdout.getvalue().strip()
        self.assertEqual("", output)
        self.assertEqual(result, [])

    def test_invalid_output_structure(self):
        result = return_wrong_structure()
        output = self.held_stdout.getvalue().strip()
        self.assertIn("Invalid output value, expected <class 'str'>!", output)

    def test_none_value(self):
        none_check(None)
        output = self.held_stdout.getvalue().strip()
        self.assertIn("Invalid input arguments, expected <class 'str'>!", output)

    def test_combined_args(self):
        result = test_func_combined_args(1, "test", c="override")
        output = self.held_stdout.getvalue().strip()
        self.assertEqual("", output)
        self.assertEqual(result, "1 test override")
        
if __name__ == '__main__':
    unittest.main()
