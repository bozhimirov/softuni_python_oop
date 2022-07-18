import unittest

from project.mammal import Mammal


class MammalTest(unittest.TestCase):
    def setUp(self) -> None:
        self.name = "name"
        self.mammal_type = 'type'
        self.sound = 'sound'
        self.kingdom = 'animals'
        self.mammal = Mammal(self.name, self.mammal_type, self.sound)

    def test_mammal_init_should_create_proper_obj(self):

        self.assertEqual(self.name, self.mammal.name)
        self.assertEqual(self.mammal_type, self.mammal.type)
        self.assertEqual(self.sound, self.mammal.sound)
        self.assertEqual('animals', self.mammal._Mammal__kingdom)

    def test_sound_gives_proper_result(self):

        actual_result = self.mammal.make_sound()
        expected_result = f'{self.name} makes {self.sound}'

        self.assertEqual(expected_result, actual_result)

    def test_get_kingdom_gives_proper_result(self):

        actual_result = self.mammal.get_kingdom()
        expected_result = 'animals'

        self.assertEqual(expected_result, actual_result)

    def test_info_gives_proper_result(self):

        actual_result = self.mammal.info()
        expected_result = f"{self.name} is of type {self.mammal_type}"

        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    unittest.main()
