import unittest
from funct_person import Person

class PersonTest(unittest.TestCase):

    def test_person(self):
        test_person = Person("Andrei",21,1.72,"Pepsi")
        expected_person_name = "Andrei"
        expected_person_age = 21
        expected_person_height = 1.72
        expected_person_drink = "Pepsi"
        self.assertEqual(test_person.name, expected_person_name)
        self.assertEqual(test_person.age, expected_person_age)
        self.assertEqual(test_person.height, expected_person_height)
        self.assertEqual(test_person.favourite_drink, expected_person_drink)

if __name__ == "main":
    unittest.main()