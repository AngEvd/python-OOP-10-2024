import unittest

from project.mammal import Mammal


class TestMammal(unittest.TestCase):
    def setUp(self):
        self.cat = Mammal("Tom", "cat", "meow")

    def test_init(self):
        self.assertEqual(self.cat.name, "Tom")
        self.assertEqual(self.cat.type, "cat")
        self.assertEqual(self.cat.sound, "meow")

    def test_make_sound(self):
        result = self.cat.make_sound()
        expected_result = "Tom makes meow"
        self.assertEqual(result, expected_result)

    def test_get_kingdom(self):
        self.assertEqual(self.cat.get_kingdom(), "animals")

    def test_info(self):
        result = self.cat.info()
        expected_result = "Tom is of type cat"
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
