import unittest

from project.train.train import Train


class TrainTest(unittest.TestCase):
    NAME = 'name'
    CAPACITY = 2
    PASSENGER_NAME = 'passenger'

    def setUp(self) -> None:
        self.train = Train(self. NAME, self.CAPACITY)

    def test_init(self):
        self.assertEqual(self.NAME, self.train.name)
        self.assertEqual(self.CAPACITY, self.train.capacity)
        self.assertEqual([], self.train.passengers)

    def test_add_if_not_capacity_raise(self):
        self.train.add('name1')
        self.train.add('name2')
        with self.assertRaises(ValueError) as err:
            self.train.add(self.PASSENGER_NAME)

        self.assertEqual(str(err.exception), "Train is full")

    def test_add_if_passenger_exists_raise(self):
        self.train.add(self.PASSENGER_NAME)
        with self.assertRaises(ValueError) as err:
            self.train.add(self.PASSENGER_NAME)

        self.assertEqual(str(err.exception), f"Passenger {self.PASSENGER_NAME} Exists")

    def test_add_correctly_added(self):
        result = self.train.add(self.PASSENGER_NAME)
        self.assertEqual(f"Added passenger {self.PASSENGER_NAME}", result)
        self.assertListEqual([self.PASSENGER_NAME], self.train.passengers)

    def test_remove_if_not_such_passenger_raise(self):
        with self.assertRaises(ValueError) as err:
            self.train.remove(self.PASSENGER_NAME)

        self.assertEqual(str(err.exception), "Passenger Not Found")

    def test_remove_successfully(self):
        self.train.add(self.PASSENGER_NAME)
        result = self.train.remove(self.PASSENGER_NAME)
        self.assertEqual(result, f"Removed {self.PASSENGER_NAME}")




