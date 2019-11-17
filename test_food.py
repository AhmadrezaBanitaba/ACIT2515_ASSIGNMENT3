import unittest
from unittest import TestCase
import inspect
from food import Food
import datetime
from menu_item_manager import MenuItemManager

class Testfood(unittest.TestCase):
    """ Unit tests for food class """

    def setUp(self):

        self.logPoint()
        self.barley_bread = Food("barley bread", 12, datetime.date(2018, 8, 8), 12.99, 149, "India", "Barley", "small",
                                 True)
        self.menu_item_manager = MenuItemManager('C:/Users/user/Desktop/ACIT2515_ASSIGNMENT3-master/test_menu.json')

    def test_food_valid(self):
        """ 010A: Valid values for constructor """
        self.logPoint()
        self.assertIsNotNone(self.barley_bread)


    def test_menu_item_description(self):
        """020A:Checks the item description"""
        self.logPoint()
        self.assertEqual(self.barley_bread.menu_item_description(), "Food item barley bread with menu index of 12 added on 2018-08-08 with the price of 12.99, containing 149 calories has a country origin of India and its main ingredient is Barley . Portion size is small and the food is vegetarian", "printed valid description" )

    def test_get_portion_size(self):
        """030A: Checks the test portion size"""
        self.logPoint()
        self.assertEqual(self.barley_bread.get_portion_size(),"small", "needs to be small")

    def test_get_main_ingredient(self):
        """040A: Check the main ingredient"""
        self.logPoint()
        self.assertEqual(self.barley_bread.get_main_ingredient(), "Barley", "needs to be Barley")

    def test_get_cuisine_country(self):
        """050A: Checks the cuisine country"""
        self.logPoint()
        self.assertEqual(self.barley_bread.get_cuisine_country(), "India", "needs to be india")

    def test_get_menu_item_name(self):
        """060A: checks the menu item name"""
        self.logPoint()
        self.assertEqual(self.barley_bread.get_menu_item_name(), "barley bread", "needs to be barley bread")

    def test_get_menu_item_no(self):
        """070A: Checks the menu item number"""
        self.logPoint()
        self.assertEqual(self.barley_bread. get_menu_item_no(), 12, "needs to be 12")

    def test_get_date_added(self):
        """080A: Checks the date added"""
        self.logPoint()
        self.assertEqual(self.barley_bread.get_date_added(), datetime.date(2018, 8, 8), "needs to be 2018,8,8")

    def test_get_price(self):
        """090A: Checks the price"""
        self.logPoint()
        self.assertEqual(self.barley_bread.get_price(), 12.99, "needs to be 12.99")

    def test_get_type(self):
        """100A: Checks the type of the menu"""
        self.logPoint()
        self.assertEqual(self.barley_bread.get_type(), "food", "needs to be drink")

    def test_to_dict(self):
        """using filepath and ensure dict is working well"""
        food_dict = self.menu_item_manager.get_all_by_type('food')

        food_menu = self.menu_item_manager.get_by_id(2)

        food_dict2 = food_menu.to_dict()

        self.logPoint()

        self.assertEqual(food_dict[0]['menu_item_name'], food_dict2['menu_item_name'], "needs to be same")
        self.assertEqual(food_dict[0]['menu_item_no'], food_dict2['menu_item_no'], "needs to be same")
        self.assertEqual(food_dict[0]['date_added'], food_dict2['date_added'], "needs to be same")
        self.assertEqual(food_dict[0]['price'], food_dict2['price'], "needs to be same")
        self.assertEqual(food_dict[0]['calories'], food_dict2['calories'], "needs to be same")
        self.assertEqual(food_dict[0]['cuisine_country'], food_dict2['cuisine_country'], "needs to be same")
        self.assertEqual(food_dict[0]['main_ingredient'], food_dict2['main_ingredient'], "needs to be same")
        self.assertEqual(food_dict[0]['portion_size'], food_dict2['portion_size'], "needs to be same")
        self.assertEqual(food_dict[0]['is_vegetarian'], food_dict2['is_vegetarian'], "needs to be same")

    def tearDown(self):

        self.logPoint()

    def logPoint(self):
        currentTest = self.id().split('.')[-1]
        callingFunction = inspect.stack()[1][3]
        print('in %s - %s()' % (currentTest, callingFunction))

if __name__ == '__main__':
    unittest.main()