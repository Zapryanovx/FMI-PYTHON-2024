import unittest
from unittest.mock import mock_open, patch
from itertools import product
from secret import validate_recipe, RuinedNikuldenDinnerError


class TestNikuldenValidator(unittest.TestCase):
    def test_valid_recipe(self):
        mock_content = "Айде от мен да мине, сготвих рибена чорба и СЬОНГА."
        with patch("builtins.open", mock_open(read_data=mock_content)):
            result = validate_recipe("някъв_файл.txt")
            self.assertTrue(result)

    def test_invalid_recipe(self):
        mock_content = "Аз тва не го ям, направих си пържоли."
        with patch("builtins.open", mock_open(read_data=mock_content)):
            result = validate_recipe("някъв_файл.txt")
            self.assertFalse(result)

    def test_bad_recipe_file(self):
        with patch("builtins.open", side_effect=OSError):
            with self.assertRaises(RuinedNikuldenDinnerError):
                validate_recipe("няма_го_този_файл.txt")

        with patch("builtins.open", side_effect=IOError ):
            with self.assertRaises(RuinedNikuldenDinnerError):
                validate_recipe("няма_го_този_файл.txt")

if __name__ == "__main__":
    unittest.main()
