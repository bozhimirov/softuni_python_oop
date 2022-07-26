from project.pet_shop import PetShop
# from pet_shop import PetShop

import unittest


class PetShopTest(unittest.TestCase):
    NAME = "name"
    VALID_QUANTITY = 1
    PET_NAME = 'pet'

    def setUp(self) -> None:
        self.petshop = PetShop(self.NAME)

    def test_init(self):
        self.assertEqual(self.petshop.name, self.NAME)
        self.assertDictEqual({}, self.petshop.food)
        self.assertListEqual([], self.petshop.pets)

    def test_add_food_quantity_0_or_less_raise(self):
        with self.assertRaises(ValueError) as error:
            self.petshop.add_food('food', self.VALID_QUANTITY - 1)
        self.assertEqual('Quantity cannot be equal to or less than 0', str(error.exception))

    def test_add_food_successfully_added_food_if_not_there(self):
        food_name = 'food'
        result = self.petshop.add_food(food_name, self.VALID_QUANTITY)
        self.assertEqual(result, f"Successfully added {self.VALID_QUANTITY:.2f} grams of {food_name}.")
        self.assertDictEqual(self.petshop.food, {'food': 1})

    def test_add_food_successfully_added_food_if_there(self):
        food_name = 'food'
        self.petshop.add_food(food_name, self.VALID_QUANTITY)
        result = self.petshop.add_food(food_name, self.VALID_QUANTITY)
        self.assertEqual(result, f"Successfully added {self.VALID_QUANTITY:.2f} grams of {food_name}.")
        self.assertDictEqual(self.petshop.food, {'food': 2})

    def test_add_pet_if_pet_not_there(self):
        result = self.petshop.add_pet(self.PET_NAME)
        self.assertListEqual(self.petshop.pets, [self.PET_NAME])
        self.assertEqual(result, f"Successfully added {self.PET_NAME}.")

    def test_add_pet_if_there_raise(self):
        self.petshop.add_pet(self.PET_NAME)
        with self.assertRaises(Exception) as error:
            self.petshop.add_pet(self.PET_NAME)
        self.assertListEqual(self.petshop.pets, [self.PET_NAME])
        self.assertEqual(str(error.exception), "Cannot add a pet with the same name")

    def test_feed_pet_if_no_pet_raise(self):
        new_name = 'new'
        self.petshop.add_pet(new_name)
        with self.assertRaises(Exception) as error:
            self.petshop.feed_pet('food', self.PET_NAME)
        self.assertEqual(str(error.exception), f"Please insert a valid pet name")
        self.assertListEqual(self.petshop.pets, [new_name])

    def test_feed_pet_if_no_food_raise(self):
        new_food = 'new'
        food_name = 'food'
        self.petshop.add_pet(self.PET_NAME)
        self.petshop.add_food(new_food, self.VALID_QUANTITY)
        result = self.petshop.feed_pet(food_name, self.PET_NAME)
        self.assertEqual(result, f'You do not have {food_name}')
        self.assertDictEqual(self.petshop.food, {new_food: 1})

    def test_feed_pet_if_food_lt_100(self):
        new_food = 'new'
        self.petshop.add_pet(self.PET_NAME)
        self.petshop.add_food(new_food, self.VALID_QUANTITY)
        result = self.petshop.feed_pet(new_food, self.PET_NAME)
        self.assertEqual(result, "Adding food...")
        self.assertDictEqual(self.petshop.food, {new_food: 1000 + self.VALID_QUANTITY})

    def test_feed_pet_if_enough_food(self):
        new_food = 'new'
        self.petshop.add_pet(self.PET_NAME)
        self.petshop.add_food(new_food, self.VALID_QUANTITY + 299)
        result = self.petshop.feed_pet(new_food, self.PET_NAME)
        self.assertEqual(result, f"{self.PET_NAME} was successfully fed")
        self.assertDictEqual(self.petshop.food, {new_food: self.VALID_QUANTITY + 299 - 100})

    def test_repr_with_pets(self):
        new_pet = 'new'
        self.petshop.add_pet(self.PET_NAME)
        self.petshop.add_pet(new_pet)
        result = repr(self.petshop)
        expected = f'''Shop {self.NAME}:
Pets: {self.PET_NAME}, {new_pet}'''
        self.assertEqual(result, expected)

    def test_repr_without_pets(self):
        result = repr(self.petshop)
        expected = f'''Shop {self.NAME}:
Pets: '''
        self.assertEqual(result, expected)
