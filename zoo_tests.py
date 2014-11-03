import unittest

from zoo import Zoo
from animal import Animal


class TestZoo(unittest.TestCase):

    def test_init(self):
        zoo = Zoo(10, 100)
        self.assertEqual(10, zoo.capacity)
        self.assertEqual(100, zoo.budget)

    def test_accommodate_animal(self):
        zoo = Zoo(10, 100)
        the_tiger = Animal("Tiger", 15, "Dingo", "male", 90)
        zoo.accommodate_animal(the_tiger)
        self.assertIn(the_tiger, zoo.animals)

    def test_cant_accommodate_animal_with_duplicate_name(self):
        zoo = Zoo(10, 100)
        the_tiger = Animal("Tiger", 15, "Dingo", "male", 90)
        the_copycat = Animal("Tiger", 15, "Dingo", "male", 90)
        zoo.accommodate_animal(the_tiger)
        with self.assertRaises(ValueError):
            zoo.accommodate_animal(the_copycat)

    def test_accomodate_same_names_diff_species(self):
        zoo = Zoo(10, 100)
        the_tiger = Animal("Tiger", 15, "Dingo", "male", 90)
        the_cat = Animal("Cat", 15, "Dingo", "male", 90)
        zoo.accommodate_animal(the_tiger)
        zoo.accommodate_animal(the_cat)
        self.assertIn(the_tiger, zoo.animals)
        self.assertIn(the_cat, zoo.animals)

    def test_get_income(self):
        zoo = Zoo(10, 100)
        the_tiger = Animal("Tiger", 15, "Dingo", "male", 90)
        the_cat = Animal("Cat", 15, "Dingo", "male", 90)
        zoo.accommodate_animal(the_tiger)
        zoo.accommodate_animal(the_cat)
        self.assertEqual(2 * zoo.ANIMAL_INCOME, zoo.get_income())


#TODO Test adding animals

if __name__ == '__main__':
    unittest.main()