import unittest

from project.vehicle import Vehicle


class VehicleTest(unittest.TestCase):
    FUEL = 100
    HORSE_POWER = 120
    DEFAULT_FUEL_CONSUMPTION = 1.25

    def setUp(self) -> None:
        self.vehicle = Vehicle(self.FUEL, self.HORSE_POWER)

    def test_vehicle_init(self):
        self.assertEqual(self.FUEL, self.vehicle.fuel)
        self.assertEqual(self.HORSE_POWER, self.vehicle.horse_power)
        self.assertEqual(self.FUEL, self.vehicle.capacity)
        self.assertEqual(self.DEFAULT_FUEL_CONSUMPTION, self.vehicle.fuel_consumption)

    def test_drive_not_enough_fuel_raise(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(100)
        self.assertEqual('Not enough fuel', str(ex.exception))
        self.assertEqual(self.FUEL, self.vehicle.fuel)

    def test_drive_reduces_fuel(self):
        distance = 50
        fuel_needed = self.DEFAULT_FUEL_CONSUMPTION * distance

        self.vehicle.drive(distance)
        expected_result = self.FUEL - fuel_needed
        self.assertEqual(expected_result, self.vehicle.fuel)

    def test_drive_reduces_fuel_with_max_possible_distance(self):
        distance = self.FUEL / self.DEFAULT_FUEL_CONSUMPTION

        self.vehicle.drive(distance)

        self.assertEqual(0, self.vehicle.fuel)

    def test_refuel_over_capacity_raises(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(self.vehicle.capacity + 1)
        self.assertEqual("Too much fuel", str(ex.exception))
    def test_refuel_increases_fuel_in_the_car(self):
        fuel_amount = 20
        self.vehicle.fuel -= fuel_amount

        self.vehicle.refuel(fuel_amount)

        self.assertEqual(self.FUEL, self.vehicle.fuel)

    def test_vehicle_str_returns_proper_results(self):
        actual = str(self.vehicle)
        expected = f"The vehicle has {self.HORSE_POWER} " \
            f"horse power with {self.FUEL} fuel left and {self.DEFAULT_FUEL_CONSUMPTION} fuel consumption"
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
