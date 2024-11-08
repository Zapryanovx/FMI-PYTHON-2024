import unittest

from halloween import HauntedMansion

class TestHauntedMansion(unittest.TestCase):
    def setUp(self):
        self.mansion = HauntedMansion(butler="Alfred", rooms=10, basement=True)

    def test_existing_attribute_with_spooky_prefix(self):
        self.assertEqual(self.mansion.spooky_butler, "Alfred")
        self.assertEqual(self.mansion.spooky_rooms, 10)
        self.assertEqual(self.mansion.spooky_basement, True)

    def test_existing_attribute_without_spooky_prefix(self):
        self.assertEqual(self.mansion.butler, "Booooo, only ghosts here!")
        self.assertEqual(self.mansion.rooms, "Booooo, only ghosts here!")
        self.assertEqual(self.mansion.basement, "Booooo, only ghosts here!")

    def test_dynamic_attribute_with_spooky_prefix(self):
        self.mansion.friendly_ghost = "Nearly Headless Nick"
        self.assertEqual(self.mansion.spooky_friendly_ghost, "Nearly Headless Nick")

    def test_dynamic_attribute_without_spooky_prefix(self):
        self.mansion.friendly_ghost = "Nearly Headless Nick"
        self.assertEqual(self.mansion.friendly_ghost, "Booooo, only ghosts here!")

    def test_missing_attribute_with_spooky_prefix(self):
        self.assertEqual(self.mansion.spooky_attic, "Booooo, only ghosts here!")

    def test_protected_attribute_with_spooky_prefix(self):
        self.mansion._hidden_treasure = "Gold"
        self.assertEqual(self.mansion.spooky__hidden_treasure, "Gold")

    def test_protected_attribute_without_spooky_prefix(self):
        self.mansion._hidden_treasure = "Gold"
        self.assertEqual(self.mansion._hidden_treasure, "Booooo, only ghosts here!")

    def test_dunder_attribute_access(self):
        self.assertEqual(self.mansion.__class__, HauntedMansion)

if __name__ == "__main__":
    unittest.main()
