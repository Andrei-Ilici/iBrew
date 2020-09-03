import unittest
from funct_drink import Drinks

class DrinkTest(unittest.TestCase):
    def test_drink(self):
        test_drink = Drinks("Evian","water","plastic",2)
        expected_drinks_name = "Evian"
        expected_drinks_category = "water"
        expected_drinks_container = "plastic"
        expected_drinks_volume = 2
        self.assertEqual(test_drink.name, expected_drinks_name)
        self.assertEqual(test_drink.category, expected_drinks_category)
        self.assertEqual(test_drink.container, expected_drinks_container)
        self.assertEqual(test_drink.volume, expected_drinks_volume)
        
if __name__ == "main":
    unittest.main()