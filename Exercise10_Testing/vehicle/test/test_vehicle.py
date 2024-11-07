from project.vehicle import Vehicle

import unittest


class TestVehicle(unittest.TestCase):
    def setUp(self):
        self.car = Vehicle(100, 150)

    def test_init(self):
        self.assertEqual(self.car.fuel, 100)
        self.assertEqual(self.car.capacity, self.car.fuel)
        self.assertEqual(self.car.horse_power, 150)
        self.assertEqual(self.car.fuel_consumption, self.car.DEFAULT_FUEL_CONSUMPTION)

    def test_drive_not_enough_fuel(self):
        with self.assertRaises(Exception) as context:
            self.car.drive(100)
        self.assertEqual(str(context.exception), 'Not enough fuel')

    def test_drive_enough_fuel(self):
        self.car.fuel = 100
        self.car.drive(10)
        expected_result = 87.5
        self.assertEqual(self.car.fuel, expected_result)

    def test_refuel_to_much_fuel(self):
        with self.assertRaises(Exception) as context:
            self.car.refuel(1000)
        self.assertEqual(str(context.exception), 'Too much fuel')

    def test_refuel_valid_fuel(self):
        self.car.fuel = 0
        self.car.refuel(50)
        self.assertEqual(self.car.fuel, 50)

    def test_str(self):
        self.car.fuel = 100
        result = self.car.__str__()
        expected_result = (f"The vehicle has 150"
                           f" horse power with 100 fuel left"
                           f" and 1.25 fuel consumption")
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
