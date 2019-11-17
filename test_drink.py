import unittest
from unittest import TestCase
import inspect
from drink import Drink
import datetime


class TestDrink(unittest.TestCase):
    """ Unit tests for drink  """

    def setUp(self):
        self.logPoint()
        self.mango_lasi3 = Drink("mango lasis", 10, datetime.date(2017, 9, 12), 12.99, 80, "lasi producer ltd", 129.99,
                                 False, False)

    def test_drink_valid(self):
        """ 010A: Valid values for constructor """
        self.logPoint()
        self.assertIsNotNone(self.mango_lasi3)

    def test_menu_item_description(self):
        """ 020A: Check that it does not return wrong description"""
        self.logPoint()
        self.assertNotEqual(self.mango_lasi3.menu_item_description(),
                         "mango lasis is a fizzy cold drink item with menu index 10 added on 2017-09-12 with the price of 12.99, containing 80 calories made by lasi producer ltd and is 129.99 ml",
                         "printed valid description")

    def test_get_manufacturer(self):
        """030A: Return the manufacturer name"""
        self.logPoint()
        self.assertEqual(self.mango_lasi3.get_manufacturer(), "lasi producer ltd", "needs to be lasi producer ltd")

    def test_get_size(self):
        """040A: checks the size of the drink"""
        self.logPoint()
        self.assertEqual(self.mango_lasi3.get_size(), 129.99, "needs to be 129.99")

    def test_get_menu_item_name(self):
        """050A: checks the menu item name"""

        self.logPoint()
        self.assertEqual(self.mango_lasi3.get_menu_item_name(), "mango lasis", "needs to be mango lasis")

    def test_get_menu_item_no(self):
        """060A: checks the menu item number"""
        self.logPoint()
        self.assertEqual(self.mango_lasi3.get_menu_item_no(), 10, "needs to be 10")

    def test_get_date_added(self):
        """070A: checks the added date"""
        self.logPoint()
        self.assertEqual(self.mango_lasi3.get_date_added(), datetime.date(2017, 9, 12), "needs to be 2017, 9 ,12")

    def test_get_price(self):
        """080A: checks get price"""
        self.logPoint()
        self.assertEqual(self.mango_lasi3.get_price(), 12.99, "needs to be 12.99")

    def test_get_type(self):
        """090A: Checks the type of the menu"""
        self.logPoint()
        self.assertEqual(self.mango_lasi3.get_type(), "drink", "needs to be drink")
        
    def test_to_dict(self):
        """ verifies to_dict method """
        pass

    def tearDown(self):
        self.logPoint()

    def logPoint(self):
        currentTest = self.id().split('.')[-1]
        callingFunction = inspect.stack()[1][3]
        print('in %s - %s()' % (currentTest, callingFunction))


if __name__ == '__main__':
    unittest.main()