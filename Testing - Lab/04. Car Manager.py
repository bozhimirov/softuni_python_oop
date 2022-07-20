import unittest


class TestCar(unittest.TestCase):
    def setUp(self) -> None:
        self.car = Car(fuel_capacity=100, fuel_consumption=5.6, make='Test', model='TestModel')

    def test_init_creates_all_attributes(self):
        self.assertEqual(100, self.car.fuel_capacity)
        self.assertEqual(5.6, self.car.fuel_consumption)
        self.assertEqual('Test', self.car.make)
        self.assertEqual('TestModel', self.car.model)
        self.assertEqual(0, self.car.fuel_amount)

    def test_init_make_null(self):
        pass

    def test_init_make_empty(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ''
        self.assertEqual('Make cannot be null or empty!', str(ex.exception))

    def test_init_make_correct(self):
        self.car.make = "new"
        self.assertEqual('new', self.car.make)


    def test_init_model_null(self):
        pass

    def test_init_model_empty_raise(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ''
        self.assertEqual('Model cannot be null or empty!', str(ex.exception))

    def test_init_model_correct(self):
        self.car.model = "new"
        self.assertEqual('new', self.car.model)

    def test_init_fuel_consumption_negative(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = -2
        self.assertEqual('Fuel consumption cannot be zero or negative!', str(ex.exception))


    def test_init_fuel_consumption_zero(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = 0
        self.assertEqual('Fuel consumption cannot be zero or negative!', str(ex.exception))

    def test_init_fuel_consumption_correct(self):
        self.car.fuel_consumption = 10
        self.assertEqual(10, self.car.fuel_consumption)


    def test_init_fuel_capacity_negative(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = -2
        self.assertEqual('Fuel capacity cannot be zero or negative!', str(ex.exception))

    def test_init_fuel_capacity_zero(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = 0
        self.assertEqual('Fuel capacity cannot be zero or negative!', str(ex.exception))

    def test_init_fuel_capacity_correct(self):
        self.car.fuel_capacity = 10
        self.assertEqual(10, self.car.fuel_capacity)


    def test_init_fuel_amount_correct(self):
        pass

    def test_init_fuel_amount_negative(self):
        pass

    def test_refuel_negative(self):
        self.assertEqual(0, self.car.fuel_amount)
        with self.assertRaises(Exception) as ex:
            self.car.refuel(-10)
        self.assertEqual('Fuel amount cannot be zero or negative!', str(ex.exception))

    def test_refuel_zero(self):
        pass

    def test_refuel_out_of_capacity_raise(self):
        pass

    def test_refuel_correct(self):
        self.assertEqual(0, self.car.fuel_amount)
        self.car.refuel(10)
        self.assertEqual(10, self.car.fuel_amount)

    def test_drive_needed_correct(self):
        self.car.refuel(100)
        self.assertEqual(100, self.car.fuel_amount)
        self.car.drive(10)
        self.assertEqual(99.44, self.car.fuel_amount)

    def test_drive_with_not_enough_fuel_rises(self):
        self.car.refuel(0.1)
        with self.assertRaises(Exception) as ex:
            self.car.drive(10)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_drive_needed_out_of_fuel_raise(self):
        self.assertEqual(0, self.car.fuel_amount)
        with self.assertRaises(Exception) as ex:
            self.car.drive(10)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))


if __name__ == "__main__":
    unittest.main()
